from django.shortcuts import redirect, render
import pandas as pd
from .models import *

def excel_import(request):
    if request.method == "POST":
        excel_file = request.FILES['excel_file']
        handle_file = HandleExcelFile.objects.create(excel_file = excel_file)
        
        datas = pd.read_excel(handle_file.excel_file)
        
        for data in datas.values.tolist():
            color_obj , _ = Color.objects.get_or_create(
                                            color_name = data[0],
                                            color_hex_code = data[1])
            fresh =  True if data[3] == 'Y' else False

            Fruits.objects.create(
                color = color_obj,
                fruit_name = data[2],
                fresh = fresh
            )
        return redirect('/excel-import/')
    return render(request , 'excel_import.html')


def excel_export(request):
    pass    