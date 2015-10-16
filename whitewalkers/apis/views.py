
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Questions, User, Response


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
    question = Questions(question_id=1+Questions.objects.latest('id').id,
                        question_text=data['question_text'],
                        template_type=data['template_type'],
                        owner_id=data['owner_id'],
                        profile=data['profile'],
                        options=options
                        )
    question.save()
    response = HttpResponse(json.dumps({
            'status': 'success',
            'data': data
        }), content_type='application/json')
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
            'data': data
        }), content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response


# def get_questions(request):
#     data = request.GET
#     uid = data['email_id']
#     #questions = mongo_query(age, gender)
#     questions = [{'question': 'GOT rocks?',
#         'template_id': 4,
#         'options': ['agree', 'disagree'],
#         'question_id': 10},
#         {'question': 'Friends rocks?',
#         'template_id': 4,
#         'options': ['agree', 'disagree'],
#         'question_id': 11},
#         {'question': 'Seinfeld rocks?',
#         'template_id': 4,
#         'options': ['agree', 'disagree'],
#         'question_id': 12},
#         {'question': 'House of cards rocks?',
#         'template_id': 4,
#         'options': ['agree', 'disagree'],
#         'question_id': 13},
#         {'question': 'Deathnote rocks?',
#         'template_id': 4,
#         'options': ['agree', 'disagree'],
#         'question_id': 14}
#     ]
#     response = HttpResponse(json.dumps(questions))
#     return response

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
