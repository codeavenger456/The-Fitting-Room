from wrnch_human import *

user = dict()
ACTUAL_HEIGHT = 100
VIRTUAL1D = ACTUAL_HEIGHT / cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height']
VIRTUAL2D = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width'] / cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height']
#y_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height']/ 100 #virtual : reality
#x_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width']/ 100 #virtual : reality

user["neck"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][33])
user["shoulder"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][26] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24])
user["hips"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][6] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]) / x_proportion
user["torsol"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][13] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15]) / y_proportion
user["legs"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][7]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5])) / 2) / y_proportion
user["tibia"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][3]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][9]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][27]) / 2
user["body_ratio"] = user["torsol"] / user["legs"]

#https://github.com/focom/wrnchtutorial/blob/master/wrnchAI_Hands_on.ipynb
#https://devportal.wrnch.ai/wrnchai_sdk/coord_spaces
