
# Create your views here.
import config
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from apis.models import Questions, User, Response
import requests
from .models import Questions, User, Response
from django.core import serializers


def get_question_data(request):
    data = request.GET
    row = Response.objects.filter(question_id=data['question_id'])
    question = Questions.objects.filter(question_id=data['question_id'])
    return_data = { question['option_1']: row['option_1'],
                    question['option_2']: row['option_2'],
                    question['option_3']: row['option_3'],
                    question['option_4']: row['option_4'],
                    question['option_5']: row['option_5']
                    }
    response = HttpResponse(json.dumps(return_data))
    return response

def get_questions_panel(request):
    data = request.GET
    questions_list = [{ 'question_id': question.question_id,
                                'question_text': question.question_text,
                                'template_type': question.template_type,
                                'owner_id': question.owner_id,
                                'profile': question.profile,
                                'options': question.options
                                } 
        for question in Questions.objects.filter(owner_id=data['owner_id'])]
    response = HttpResponse(json.dumps(questions_list))
    return response

@csrf_exempt
def push_question(request):
    data = request.POST
    options = data.getlist('options')
    try:
    	question_id = 1+Questions.objects.latest('id').id
    except:
    	question_id = 1
    question = Questions(question_id=question_id,
                        question_text=data['question_text'],
                        template_type=data['template_type'],
                        owner_id=data['owner_id'],
                        profile=data['profile'],
                        options=options
                        )
    question.save()
    response = HttpResponse(json.dumps({
            				'status': 'success',
				            'data': data}),
				             content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

@csrf_exempt
def fetch_user_profile(request):
    data = request.POST
    # import ipdb
    # ipdb.set_trace()
    user_id = data.get('user_id', None)
    gender = data.get('gender', None)
    age = data.get('age', None)
    user = User(user_id=user_id, gender=gender, age=age)
    user.save()
    response = HttpResponse(json.dumps({
                           'status': 'success',
            				'data': data}),
        					 content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def get_user_profile(request):
    data = request.GET
    user_id = data.get('user_id', None)
    user = User.objects.get(user_id = user_id)
    profile = {'age': str(user.age), 'gender': str(user.gender)}
    response = HttpResponse(json.dumps(profile))
    return response

def match_profile(profile, question_profile):
	for filters in question_profile:
		if filters == 'age':
			if int(profile[filters]) not in range(int(question_profile[filters]['min']), 
				int(question_profile[filters]['max'])):
				return False
		elif question_profile[filters] != profile[filters]:
			return False
	return True

def get_questions_extension(request):
	data = request.GET
	user_id = data.get('user_id', None)
	base_url = config.server_url+'/get_user_profile'
	profile = requests.get(base_url, params = {'user_id': str(user_id)}).json()
	question_list = Questions.objects.all()
	suggested_questions  = []
	# import ipdb
	# ipdb.set_trace()
	for question in question_list:
		question = json.loads(serializers.serialize('json', [ question, ]))[0]
		if match_profile(profile, json.loads(question['fields'].get('profile', None))):
			suggested_questions.append(question)
	response = HttpResponse(json.dumps(suggested_questions))
	return response
	# questions = [{'question': 'GOT rocks?',
	# 	'template_id': 4,
	# 	'options': ['agree', 'disagree'],
	# 	'question_id': 10},
	# 	{'question': 'Friends rocks?',
	# 	'template_id': 4,
	# 	'options': ['agree', 'disagree'],
	# 	'question_id': 11},
	# 	{'question': 'Seinfeld rocks?',
	# 	'template_id': 4,
	# 	'options': ['agree', 'disagree'],
	# 	'question_id': 12},
	# 	{'question': 'House of cards rocks?',
	# 	'template_id': 4,
	# 	'options': ['agree', 'disagree'],
	# 	'question_id': 13},
	# 	{'question': 'Deathnote rocks?',
	# 	'template_id': 4,
	# 	'options': ['agree', 'disagree'],
	# 	'question_id': 14}
	# ]

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
