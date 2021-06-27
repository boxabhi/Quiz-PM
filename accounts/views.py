from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from .utils import send_activation_email
import uuid
from .thread import *

# token -> 24hr  - [ active ] ! [error invalid token token expired]

def register(request):

    if request.method == 'POST':
        email   = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        email_token = uuid.uuid4()
        
        user_obj = User(
            email = email, 
            phone_number = phone_number,
            email_token = email_token,
        )
        user_obj.set_password(password)
        user_obj.save()

        activation_url = f'http://127.0.0.1:8000/verify/{email_token}/'

    
 
        messages.info(request, 'Account created.')
        return redirect('/login/')

    return render(request, 'register.html')



def verify_user_account(request , token):
    try:
        if not cache.get(token):
            return HttpResponse('Your token has expired or invalid')
        
        print(cache.ttl(token)) 

        user_obj = User.objects.get(email_token = token)
        user_obj.is_verified = True
        user_obj.save()
        return HttpResponse('Your account is verified')
    except Exception as e:
        print(e)
    return HttpResponse('Invalid Token')

def login_attempt(request):
    if request.method == 'POST':
        email   = request.POST.get('email')
        password = request.POST.get('password')



    return render(request , 'login.html')