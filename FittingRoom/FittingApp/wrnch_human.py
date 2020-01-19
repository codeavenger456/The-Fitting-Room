
import requests     

import json

import time




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

  resp_sub_job = requests.post(JOBS_URL,

                              headers={'Authorization':f'Bearer {JWT_TOKEN}'},

                              files={'media':f},

                              data={'work_type':'json'}

                              )



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

#cloud_xLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][30]

#cloud_xLKNEE = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][8]



#print(cloud_xLWRIST)    # 0.7735621333122253

#print(cloud_xLKNEE)     # 0.7657291889190674