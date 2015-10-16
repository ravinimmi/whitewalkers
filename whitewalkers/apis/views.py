
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Questions, User


def get_questions(request):
    data = request.GET
    # uid = data['uid']
    # if 'age' in data:
    #     age = data['age']
    # if 'gender' in data:
    #     gender = data['gender']
    #questions = mongo_query(age, gender)
    questions = {'lol':'cool_question'}
    response = HttpResponse(json.dumps(questions))
    return response

def send_questions(request):
    # data = request.GET
    # owner_id = data['owner_id']
    question_objects_list = Questions.objects.all()
    questions_list = []
    for question in question_objects_list:
        questions_list.append({ 'question_id': question.question_id,
                                'question_text': question.question_text,
                                'template_type': question.template_type,
                                'owner_id': question.owner_id,
                                'profile': question.profile,
                                'option_1': question.option_1,
                                'option_2': question.option_2,
                                'option_3': question.option_3,
                                'option_4': question.option_4,
                                'option_5': question.option_5,
                                })
    # output = [p.question_text for p in question_objects_list]
    response = HttpResponse(json.dumps(questions_list))
    return response

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
#   data = request.POST
