from django.shortcuts import render

# Create your views here.

import os
from django.http import HttpResponse
from . import mid


def process_audio(request):
    response = HttpResponse()

    if request.method == 'POST':

        file_path = request.POST.get('file_path', "")
        min_main = request.POST.get('min_main', "")
        max_main = request.POST.get('max_main', "")
        control = request.POST.get('control', "")
        mild = request.POST.get('mild', "")
        save_path = request.POST.get('save_path', '')

        if file_path == "" or min_main == "" or max_main == "" or control == "" or mild == "":
            response.status_code = 400
            response.content = "Params wrong:please check the necessary params"
        else:
            try:
                min_main = int(min_main)
            except:
                response.status_code = 400
                response.content = 'invalid parameters:min_main,con not convert to int type'

            else:
                try:
                    max_main = int(max_main)
                except:
                    response.status_code = 400
                    response.content = 'invalid parameters:max_main,con not convert to int type'
                else:
                    try:
                        control = int(control)
                    except:
                        response.status_code = 400
                        response.content = 'invalid parameters:control,con not convert to int type'
                    else:
                        response.status_code = 200
                        response.content = mid.process_audio(file_path, min_main, max_main, control, mild, save_path)

    return response
