from django.contrib import admin

# Register your models here.
from .models import *


class FruitsAdmin(admin.ModelAdmin):
    list_display = ['color'  , "fruit_name",
"fresh" ]

admin.site.register(Color)
admin.site.register(Fruits , FruitsAdmin)