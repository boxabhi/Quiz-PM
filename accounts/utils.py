from django.conf import settings
from django.core.mail import send_mail
import time




def send_activation_email(email , first_name , activation_url):
    time.sleep(20)
    try:
        subject = 'Your accounts needs to verified'
        message = f'Hi {first_name}, click on the link to activate your account {activation_url}'
        email_from = settings.EMAIL_HOST
        send_mail(subject , message ,email_from ,[email])

    except Exception as e:
        print(e)
        



