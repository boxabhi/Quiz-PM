from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self , email , password =None , **extra_fields):
        if not email:
            raise ValueError('This field is required')
        
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self , email , password , **extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be true in admin')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be true in admin')

        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must be true in admin')

        return self.create_user(email , password , **extra_fields)


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super(EmployeeManager , self).get_queryset().filter(type = 'F')
    
    def create(self , **kwargs):
        kwargs.update({'type' : 'F'})
        return super(EmployeeManager , self).create(**kwargs)
        