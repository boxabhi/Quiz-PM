from django.db import models
import uuid
import random
from django.contrib.auth import get_user_model


# DRY -> Object-> Inheritance 

class Payments(models.Model):
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True



class Category(BaseModel):
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category




class User(BaseModel):
    user_name = models.CharField(max_length=100 )
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user_name


class QuestionModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    


class Question(BaseModel):
    category= models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True)
    question = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    
    # objects = QuestionModelManager()
    # admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.question

    def get_answer(self):
        answers_objs = Answer.objects.filter(question = self)
        answers_objs = list(answers_objs)
        random.shuffle(answers_objs)
 
        payload = []
        for answers_obj in answers_objs:
            payload.append({
                'id' : answers_obj.id,
                'answer' : answers_obj.answer
            })
        return payload


class Answer(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


class Quiz(BaseModel):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , blank=True)
    
    

class QuizQuestion(BaseModel):
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE , null=True , blank=True)
    question = models.ForeignKey(Question ,  on_delete=models.CASCADE , null=True , blank=True)
    correct_answer = models.ForeignKey(Answer ,  on_delete=models.CASCADE , null=True , blank=True)



class QuestionAttempted(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz , on_delete=models.SET_NULL , null=True , blank=True)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    

