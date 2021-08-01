import threading
from django.conf import settings
from django.core.mail import send_mail
import time
# from django.core.cache import cache


class SendAccountActivationEmail(threading.Thread):
    def __init__(self , email , first_name , activation_url , token):
        self.email = email
        self.first_name = first_name
        self.activation_url = activation_url
        self.token = token
        threading.Thread.__init__(self)


    def run(self):
        print('INSIDE SLEEP')
        time.sleep(20)
        print('OUT FROM SLEEP')
        try:
            subject = 'Your accounts needs to verified'
            message = f'Hi {self.first_name}, click on the link to activate your account {self.activation_url}'
            email_from = settings.EMAIL_HOST
            print('SEND EMAIL STARTED')
            # cache.set(self .token , self.email, timeout=120)
            send_mail(subject , message ,email_from ,[self.email])
            print('EMAIL SENT')
        except Exception as e:
            print(e)


# 1:00 PM 23  1:01 PM 23