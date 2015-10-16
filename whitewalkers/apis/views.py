
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from apis.models import Questions, User, Response


def get_question_data(request):
    data = request.GET
    response = Response.objects.filter(question_id=data['question_id'])[0]
    response = {'question_id': response.question_id,
                'options': json.loads(response.options)}
    response = HttpResponse(json.dumps(response))
    return response


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
    user_id = data['user_id']
    gender = data['gender']
    age = data['age']
    user = User(user_id=user_id, gender=gender, age=age)
    user.save()
    response = HttpResponse(json.dumps({
                           'status': 'success',
                            'data': data}),
                             content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
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
