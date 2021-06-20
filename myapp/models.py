from django.db import models


class HandleExcelFile(models.Model):
    excel_file = models.FileField(upload_to="excel")

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    color_hex_code = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.color_name

class Fruits(models.Model):
    color = models.ForeignKey(Color , on_delete=models.SET_NULL , null=True)
    fruit_name = models.CharField(max_length=100)
    fresh = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.fruit_name



