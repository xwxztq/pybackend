from django.shortcuts import render

# Create your views here.

import os
import base64_decode
import datetime
from django.http import HttpResponse
from . import mid
from pybackend.settings import MEDA_PATH


def process_audio(request):
    response = HttpResponse()

    if request.method == 'POST':


        file = request.POST.get('file')
        min_main = request.POST.get('minmain', "")
        max_main = request.POST.get('maxmain', "")
        control = request.POST.get('control', "")
        mild = request.POST.get('mild', "")
        save_path = request.POST.get('savepath', '')


        # todo : filepath wasn't been

        if file is None or min_main == "" or max_main == "" or control == "" or mild == "":
            response.status_code = 400
            response.content = "Params wrong:please check the necessary params"
        else:

            the_content,the_format = base64_decode.transfer(file)
            pure_name = str(datetime.datetime.now())

            fname = os.path.join(MEDA_PATH,the_format,pure_name+'.'+the_format)

            with open(fname,'wb') as fout:
                fout.write(the_content)

            if the_format != "mid":
                response.status_code = 400
                response.content = "Format is incorrect"
                return response

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
                        response.content = mid.process_audio(fname, min_main, max_main, control, mild, save_path)
    else:
        response.status_code = 400
        response.content = "Wrong way to get source"

    return response
