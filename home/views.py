from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.db import transaction
from django.http import JsonResponse, request
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from django.core.cache import cache


def home(request):
    context = {}
    if cache.get('categories'):
        context['categories'] = cache.get('categories')
        print('CALLED FROM CACHE')
    else:
        context['categories'] = Category.objects.all()
        cache.set('categories' , context['categories'])
        print('CALLED FROM DB')
        
    return render(request, 'home.html'  , context)


def create_question(request , quiz_id):
    context = {'quiz_id' : quiz_id , 'category' : request.GET.get('category')}
    return render(request  , 'quiz.html')



def get_questions(request):
    category = request.GET.get('category')

    questions_objs = Question.objects.all()
    if category:
        questions_objs = questions_objs.filter(category__category__icontains = category)

    questions_objs = list(questions_objs)

    random.shuffle(questions_objs)

    payload = []
    for questions_obj in questions_objs:
        payload.append({
            'id' : questions_obj.id,
            'category' :questions_obj.category.category,
            'question' : questions_obj.question,
            'is_active' : questions_obj.is_active,
            'answer' : questions_obj.get_answer()
        })
       
    return JsonResponse({'status' : 200 , 'questions' : payload} , safe = False)


from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
@api_view(['POST'])
def create_quiz(request):
    result = {'message' : 'something went wrong' , 'status' : False}
    try:
        data =  json.loads(request.body) # request.data

        user_name = data.get('user_name')
        category = data.get('category_id')

        if category is None or user_name is None:
            result['message'] = 'category and user_name is required'
            raise Exception('category and user_name is required')


        user_obj , _ = User.objects.get_or_create(user_name = user_name)
        category_obj = None
        try:
            category_obj = Category.objects.get(id = category)

        except Exception as e:
            result['message'] = 'invalid category id'
            return JsonResponse(result)

        quiz_obj = Quiz.objects.create(user = user_obj , category = category_obj)
        
        result['message'] = 'Your quiz is created'
        result['data'] = {'quiz_id' : quiz_obj.id , 'category' : category_obj.category }
        result['status'] = True

        return JsonResponse(result)

    except Exception as e:
        print(e)

    return JsonResponse(result)


@api_view(['POST'])
def store_quiz(request , quiz_id):
    result = {'message' : 'something went wrong' , 'status' : False}
    try:
        data = request.data

        quiz_obj = Quiz.objects.get(id = quiz_id)
        question_id = data.get('question_id')
        answer_id = data.get('correct_answer')

        if question_id is None or answer_id is None:
            result['message'] = 'question_id and answer_id is required'
            raise Exception('question_id and answer_id is required')


        question_obj = None
        answer_obj = None

        try:
            question_obj = Question.objects.get(id = question_id)
            answer_obj = Answer.objects.get(id = answer_id)
        except Exception as e:
            print(e)
            result['message'] = 'invalid question id or answer id'
            return Response(result)



        QuizQuestion.objects.create(
            quiz = quiz_obj,
            question =  question_obj,
            correct_answer = answer_obj,
        )

        result['message'] = 'question added'
        result['status'] = True

        return Response(result)

    except Exception as e:
        print(e)
    return Response(result)


