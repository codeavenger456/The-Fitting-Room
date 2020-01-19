from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import User
import requests     
import json
import time
from django.http import HttpResponse

# Create your views here.
def index(request, name, gender, height):
    data = {"personName": name}
    u = User(name = name, gender = gender, height = height)
    u.save()
    if request.method == 'POST':    
        upload_file = request.FILES['selfie']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        LOGIN_URL = 'https://api.wrnch.ai/v1/login'

        JOBS_URL = 'https://api.wrnch.ai/v1/jobs'

        API_KEY = '1d0efdb9-addd-4514-a66e-c88b9e8bdcd1' # Go to https://devportal.wrnch.ai/licenses, click on the key icon to find your cloud API key



        resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})

        #print(resp_auth.text)

        # the jwt token is valid for an hour

        JWT_TOKEN = json.loads(resp_auth.text)['access_token']



        # {"access_token": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

        #                   bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

        #                   ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"}

        filename = './media/' + upload_file.name

        with open(filename, 'rb') as f:

            resp_sub_job = requests.post(JOBS_URL, headers={'Authorization':f'Bearer {JWT_TOKEN}'},files={'media':f},data={'work_type':'json'})



        job_id = json.loads(resp_sub_job.text)['job_id']

        #print('Status code:',resp_sub_job.status_code)  # Status code: 202

        #print('Response:',resp_sub_job.text)            # Response: {"job_id": "f1cdaa7f-4823-49e1-9a26-382058278e35"}



        # wait a few seconds to retrieve the result

        # you could check the job status in this link https://devportal.wrnch.ai/jobs OR using following command



        GET_JOB_STATUS_URL = 'https://api.wrnch.ai/v1/status' + '/' + job_id

        response = requests.get(GET_JOB_STATUS_URL, headers={'Authorization':f'Bearer {JWT_TOKEN}'})

        #print('Job status:', response.text)



        time.sleep(3)



        GET_JOB_URL = JOBS_URL + '/' + job_id

        #print(GET_JOB_URL)

        resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})

        #print('Status code:',resp_get_job.status_code)

        #print('\nResponse:',resp_get_job.text)
        cloud_pose_estimation = json.loads(resp_get_job.text)
        user = dict()
        ACTUAL_HEIGHT = float(User.objects.last().height)
        ACTUAL_WIDTH = float(ACTUAL_HEIGHT) * cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width'] / cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height']
        x_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width'] / ACTUAL_WIDTH
        y_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height'] / ACTUAL_HEIGHT

        user["neck"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][33]) / y_proportion
        user["shoulder"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][26] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24]) / x_proportion
        user["hips"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][6] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]) / x_proportion
        user["torsol"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][13] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15]) / y_proportion
        user["legs"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][7]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5])) / 2) / y_proportion
        #user["tibia"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][3]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][9]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][27]) / 2
        left = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][3]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]
        right = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][9]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][27]
        user["tibia"] = (left + right) / 2 / y_proportion
        user["body_ratio"] = user["torsol"] / user["legs"]
        return HttpResponse(json.dumps(user))

    return render(request, 'FittingApp/index.html', data)