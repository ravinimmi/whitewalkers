import config
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from apis.models import Questions, User, Response
import requests
from .models import Questions, User, Response, QuestionAndUser
from django.core import serializers
from datetime import date
import datetime

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
                                'options': question.options,
                                'flag': question.flag,
                                'target': question.target
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
                        options=data.getlist('options'),
                        flag = data['flag'],
                        target = data['target']
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
def push_user_profile(request):
    data = request.POST
    user_id = data.get('user_id', None)
    gender = data.get('gender', None)
    try:
        birthday_str = data.get('birthday', None)
        birthday = datetime.datetime.strptime(birthday_str, '%m/%d/%Y').date()
        age = calculate_age(birthday)
    except:
        age = 25

    user = User.objects.all().filter(user_id=user_id)
    if user.exists():
        user = user[0]
        user.gender = gender
        user.age = age
    else:
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
    for question in question_list:
        question = json.loads(serializers.serialize('json', [ question, ]))[0]
        if QuestionAndUser.objects.filter(question_id = question['fields']['question_id'], user_id = user_id).exists():
            continue
        elif match_profile(profile, json.loads(question['fields'].get('profile', None))):
            suggested_questions.append(question)
            q_user = QuestionAndUser(question_id = question['fields']['question_id'], user_id = user_id)
            q_user.save()
    response = HttpResponse(json.dumps(suggested_questions))
    return response

def get_profile_key(question_id):
    for k,v in config.profile_questions.iteritems():
        if v == question_id:
            return k
    return 'no_key'

@csrf_exempt
def send_response(request):
    data = request.POST
    options_selected = data.getlist('options')

    # try:
    #   response = Response.objects.filter(question_id=data['question_id'])[0]
    # except ProgrammingError:
    #   response = Response(question_id=data['question_id'], options=json.dumps(options_selected))

    if Response.objects.filter(question_id=data['question_id']).exists():
        response = Response.objects.filter(question_id=data['question_id'])[0]
        response_options = json.loads(response.options)
        for option in options_selected:
            if option not in response_options:
                response_options[option] = 1
            else:
                response_options[option] = int(response_options[option])+1
    else:
        options_list = []
        for option in options_selected:
            options_list.append({option: 1})
        response = Response(question_id=data['question_id'], options=options_list,
            user_id = data['user_id'])      

    if Questions.objects.filter(question_id = data['question_id']).flag == 'user_profile':
        profile_key = get_profile_key(data['question_id'])
        if profile_key is not 'no_key':
            value = data['profile_key']
            if profile_key == 'profession_type':
                User.objects.filter(data['user_id']).update(profession_type = value)
            if profile_key == 'interests':
                User.objects.filter(data['user_id']).update(interests = value)
            if profile_key == 'education':
                User.objects.filter(data['user_id']).update(education = value)

    return_data = HttpResponse(json.dumps({
            'status': 'success',
            'data': data
        }), content_type='application/json')
    return_data['Access-Control-Allow-Origin'] = '*'
    return return_data

#TODO
#get_template_api
#get_response_api
