
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

def fetch_user_profile(request):
	data = request.GET
	uid = data['uid']
	# query_output  = mongo_query('uid')
	query_output = {'lol':'cool app'}
	response = HttpResponse(json.dumps(query_output))
	return response

def get_questions(request):
	data = request.GET
	uid = data['uid']
	if 'age' in data:
		age = data['age']
	if 'gender' in data:
		gender = data['gender']
	#questions = mongo_query(age, gender)
	questions = {'lol':'cool_question'}
	response = HttpResponse(json.dumps(questions))
	return response

def get_templates(request):
	data = request.GET
	templates = {'yolo': 'template_list'}
	response = HttpResponse(json.dumps(templates))
	return response