from wrnch_human import *

user = dict()
ACTUAL_HEIGHT = height
ACTUAL_WIDTH = ACTUAL_HEIGHT * cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width'] / cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height']
x_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['width'] / ACTUAL_WIDTH
y_proportion = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['bbox']['height'] / ACTUAL_HEIGHT

user["neck"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][33]) / y_proportion
user["shoulder"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][26] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][24]) / x_proportion
user["hips"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][6] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][4]) / x_proportion
user["torsol"] = (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][13] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][15]) / y_proportion
user["legs"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][7]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][5])) / 2) / y_proportion
user["tibia"] = (((cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][1] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][3]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][25]) + (cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][11] + cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][9]) / 2 - cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][27]) / 2
user["body_ratio"] = user["torsol"] / user["legs"] / y_proportion

#https://github.com/focom/wrnchtutorial/blob/master/wrnchAI_Hands_on.ipynb
#https://devportal.wrnch.ai/wrnchai_sdk/coord_spaces
