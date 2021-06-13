from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.db import transaction
from django.http import JsonResponse
import random

def home(request):
    if request.method == 'POST':
        try:
            user_one = request.POST.get('user_one')
            user_two = request.POST.get('user_two')
            amount = request.POST.get('amount')
            with transaction.atomic():
                user_one_obj = Payments.objects.get(user = user_one)
                user_one_obj.amount -= int(amount)
                user_one_obj.save()

                user_two_obj = Payments.objects.get(user = user_two)
                user_two_obj.amount += int(amount)
                user_two_obj.save()
                messages.success(request, 'Your amount is transfered')

        except Exception as e:
            print(e)
            messages.success(request, 'Something went wrong.')


        return redirect('/')
    return render(request, 'home.html')




def get_questions(request):
    questions_objs = Question.objects.all()
    questions_objs = list(questions_objs)
    random.shuffle(questions_objs)
    payload = []
    for questions_obj in questions_objs:
        payload.append({
            'id' : questions_obj.id,
            'question' : questions_obj.question,
            'is_active' : questions_obj.is_active,
            'answer' : questions_obj.get_answer()
        })
        
    return JsonResponse({'status' : 200 , 'questions' : payload} , safe = False)
