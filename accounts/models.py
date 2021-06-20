
from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User , AbstractUser
from django.db.models.fields import proxy
from .manager import *

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique= True)
    is_verified = models.BooleanField(default = False)
    phone_number = models.CharField(max_length=12)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class BaseEmployee(models.Model):
    EmployeeType = (('F' , 'Full time' ) , ('P' , 'Part Time'))
    name = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.CharField(max_length=10)
    type = models.CharField(choices=EmployeeType , max_length=10  )



class Employee(BaseEmployee):
    objects = EmployeeManager()
    object2 = models.Manager

    class Meta:
        proxy = True


