import threading
from django.conf import settings
from django.core.mail import send_mail
import time

class SendAccountActivationEmail(threading.Thread):
    def __init__(self , email , first_name , token):
        self.email = email
        self.first_name = first_name
        self.activation_url = token
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(20)
        try:
            subject = 'Your accounts needs to verified'
            message = f'Hi {self.first_name}, click on the link to activate your account {self.activation_url}'
            email_from = settings.EMAIL_HOST
            print('SEND EMAIL STARTED')
            send_mail(subject , message ,email_from ,[self.email])
            print('EMAIL SENT')
        except Exception as e:
            print(e)

