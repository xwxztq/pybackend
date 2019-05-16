from django.shortcuts import render

# Create your views here.

import os
import json
import base64_decode
import datetime
from django.http import HttpResponse
from . import mid
from pybackend.settings import MEDA_PATH,GET_HEAD


def process_audio(request):
    response = HttpResponse()

    if request.method == 'POST':

        payload  = None

        for i in request:
            print(type(i),i)
            if len(i) >20:
                payload = i
                break

        the_dict = json.loads(payload)
        files =the_dict['file']
        min_main = dd['minmain']
        max_main = dd['maxmain']
        control = dd['control']
        mild = dd['mild']


        # todo : filepath wasn't been

        if files is None or min_main == "" or max_main == "" or control == "" or mild == "":
            response.status_code = 400
            response.content = "Params wrong:please check the necessary params"
        else:

            the_content,the_format = base64_decode.transfer(files)
            pure_name = str(datetime.datetime.now())

            fname = os.path.join(MEDA_PATH,the_format,pure_name+'.'+the_format)
            save_path = os.path.join(MEDA_PATH, the_format, pure_name+'pro.'+the_format)

            with open(fname,'wb') as fout:
                fout.write(the_content)

            if the_format != "mid":
                response.status_code = 400
                response.content = "Format is incorrect"
                return response

            min_main = int(min_main)
            max_main = int(max_main)
            control = int(control)
            mid.process_audio(fname, min_main, max_main, control, mild, save_path)
            response.status_code = 200
            ret_path = GET_HEAD + the_format +'/' + pure_name +'pro.'+the_format
            print(ret_path)
            response.content =  ret_path
    else:
        response.status_code = 400
        response.content = "Wrong way to get source"

    return response
