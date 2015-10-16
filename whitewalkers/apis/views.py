
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def fetch_user_profile(request):
	data = request.POST
	#uid = data['email_id']
	# query_output  = mongo_query('uid')
	response = HttpResponse(json.dumps({
            'status': 'success',
            'data': data
        }), content_type='application/json')
	print data, '2'
	response['Access-Control-Allow-Origin'] = '*'
	return response
	

def get_questions(request):
	data = request.GET
	uid = data['email_id']
	#questions = mongo_query(age, gender)
	questions = [{'question': 'GOT rocks?',
		'template_id': 4,
		'options': ['agree', 'disagree'],
		'question_id': 10},
		{'question': 'Friends rocks?',
		'template_id': 4,
		'options': ['agree', 'disagree'],
		'question_id': 11},
		{'question': 'Seinfeld rocks?',
		'template_id': 4,
		'options': ['agree', 'disagree'],
		'question_id': 12},
		{'question': 'House of cards rocks?',
		'template_id': 4,
		'options': ['agree', 'disagree'],
		'question_id': 13},
		{'question': 'Deathnote rocks?',
		'template_id': 4,
		'options': ['agree', 'disagree'],
		'question_id': 14}
	]
	response = HttpResponse(json.dumps(questions))
	return response

@csrf_exempt
def get_response(request):
	data = request.POST
	print data, '1'
	# import ipdb
	# ipdb.set_trace()
	response = HttpResponse(json.dumps({
            'status': 'success',
            'data': data
        }), content_type='application/json')
	print data, '2'
	response['Access-Control-Allow-Origin'] = '*'
	return response
	

def get_templates(request):
	data = request.GET
	templates = {'yolo': 'template_list'}
	response = HttpResponse(json.dumps(templates))
	return response

# def post_questions_from_panel(request):
# 	data = request.POST
