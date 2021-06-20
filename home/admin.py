from django.contrib import admin

# Register your models here.
from .models import *

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount']



class ChoiceAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ ChoiceAdmin ]
    


admin.site.register(Payments , PaymentAdmin)
admin.site.register( Question, QuestionAdmin )
admin.site.register(Category)
admin.site.register(Quiz)