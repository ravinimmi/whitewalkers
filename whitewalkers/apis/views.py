
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from .models import Questions, User

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fetch_user_profile(request):
    data = request.POST
    # user_id = data['user_id']
    # age = data['age']
    # gender = data['gender']
    # user = User(user_id=user_id, gender=gender, age=age)
    # user.save()
    print data
    response = HttpResponse(json.dumps(data))
    return response

def get_questions(request):
    data = request.GET
    # uid = data['uid']
    if 'age' in data:
        age = data['age']
    if 'gender' in data:
        gender = data['gender']
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

def get_templates(request):
    data = request.GET
    templates = {'yolo': 'template_list'}
    response = HttpResponse(json.dumps(templates))
    return response

# def post_questions_from_panel(request):
#   data = request.POST
