from django.http.response import HttpResponse
from django.shortcuts import redirect, render
  
from django.contrib import messages
from .utils import send_activation_email
import uuid
from .thread import *
from django.contrib.auth import get_user_model
User = get_user_model()

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


        SendAccountActivationEmail(email ,'Abhijeet' , activation_url ,email_token).start()
        
        #send_activation_email(email ,'Abhijeet' , activation_url )   
 
        messages.info(request, 'Account created.')
        return redirect('/login/')

    return render(request, 'register.html')



def verify_user_account(request , token):
    try:
        user_obj = User.objects.get(email_token = token)
        if user_obj.is_verified:
            return HttpResponse('Your account is already verified')
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