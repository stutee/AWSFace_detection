import boto3
import base64
import json
import os


rekognition_client=boto3.client('rekognition')

file=open('stu.jpg','rb').read()
#performs detection of the faces:the input image passed as base64-encoded image bytes 
response = rekognition_client.detect_faces(
	Image={
		'Bytes': file
		},
		Attributes=['ALL']
)

for face in response['FaceDetails']:
	print('The age is between: ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + ' years')
	print('The face is of: ' + str(face['Gender']['Value']))

	Sunglass = str(face['Sunglasses']['Value'])

	if Sunglass == 'True':
		print('It is wearing sunglass')
	else:
		print('It is not wearing sunglass')
#exploring different attributes
	print('The face has beard? ' + str(face['Beard']['Value']))
	print('The face has mustache? ' + str(face['Mustache']['Value']))
	print('The face has open eyes? ' + str(face['EyesOpen']['Value']))
	print("Emotions: {}".format(face['Emotions'][0]['Type']))
	


	