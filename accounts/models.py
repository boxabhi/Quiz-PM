
from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User , AbstractUser
from .manager import *

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique= True)
    is_verified = models.BooleanField(default = False)
    phone_number = models.CharField(max_length=12)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# class Student(User):
#     student_id = models.CharField(max_length=100)
#     branch_name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name  = 'Student'


# class Teacher(User):
#     teacher_id = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     subject = models.CharField(max_length=100)
#     adhar_card = models.CharField(max_length=100)

#     class Meta:
#         verbose_name  = 'education_teacher'

# class Staff(User):
#     staff_id = models.CharField(max_length=100)
#     class Meta:
#         verbose_name  = 'Staff'

