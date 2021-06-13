from django.db import models
import uuid
import random


class Payments(models.Model):
    user = models.CharField(max_length=100)
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
    

class User(BaseModel):
    user_name = models.CharField(max_length=100 )


class Question(BaseModel):
    category= models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True)
    question = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
  
    def get_answer(self):
        answers_objs = Answer.objects.filter(question = self)
        answers_objs = list(answers_objs)
        random.shuffle(answers_objs)
 
        payload = []
        for answers_obj in answers_objs:
            payload.append({
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
    










