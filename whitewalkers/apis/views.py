
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
from datetime import date

def get_question_data(request):
    data = request.GET
    response = Response.objects.filter(question_id=data['question_id'])[0]
    response = {'question_id': response.question_id,
                'options': json.loads(response.options)}
    response = HttpResponse(json.dumps(response))
    return response

def calculate_age(born):
	today = date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_questions_panel(request):
    data = request.GET
    questions_list = [{ 'question_id': question.question_id,
                                'question_text': question.question_text,
                                'template_type': question.template_type,
                                'owner_id': question.owner_id,
                                'profile': json.loads(question.profile),
                                'options': question.options
                                } 
        for question in Questions.objects.filter(owner_id=data["owner_id"])]
    response = HttpResponse(json.dumps(questions_list))
    return response

@csrf_exempt
def push_question(request):
    data = request.POST
    try:
        question_id = 1+Questions.objects.latest('id').id
    except:
        question_id = 1
    question = Questions(question_id=question_id,
                        question_text=data['question_text'],
                        template_type=data['template_type'],
                        owner_id=data['owner_id'],
                        profile=data['profile'],
                        options=data.getlist('options')
                        )
    question.save()
    option_clicks = {option: 0 for option in data.getlist('options')}
    response = Response(question_id=question_id, options=json.dumps(option_clicks))
    response.save()
    response = HttpResponse(json.dumps({
                            'status': 'success',
                            'data': data}),
                             content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

@csrf_exempt
def fetch_user_profile(request):
    data = request.POST
    import ipdb
    ipdb.set_trace()
    user_id = data.get('user_id', None)
    gender = data.get('gender', None)
    try:
    	birthday_str = data.get('birthday', None)
    	birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()
    	age = calculate_age(birthday)
    except:
    	age = 25
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

@csrf_exempt
def send_response(request):
    data = request.POST
    options_selected = data.getlist('options')
    response = Response.objects.filter(question_id=data['question_id'])[0]
    response_options = json.loads(response.options)
    response.delete()
    for option in options_selected:
        response_options[option] = 1+response_options[option]
    response = Response(question_id=data['question_id'], options=json.dumps(response_options))
    response.save()
    return_data = HttpResponse(json.dumps({
            'status': 'success',
            'data': data
        }), content_type='application/json')
    return_data['Access-Control-Allow-Origin'] = '*'
    return return_data
