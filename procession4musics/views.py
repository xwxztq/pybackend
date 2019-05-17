from django.shortcuts import render

# Create your views here.

import os
import json
import base64_decode
import datetime
from django.http import HttpResponse
from . import mid
from pybackend.settings import MEDA_PATH,GET_HEAD
from .style_transfer import Transfer


def process_audio(request):
    response = HttpResponse()

    if request.method == 'POST':

        payload = None

        for i in request:
            print(type(i), i)
            if len(i) > 20:
                payload = i
                break

        dd = json.loads(payload)
        the_file = dd['file']
        the_style = dd['targetStyle']

        if the_file is None:
            response.status_code = 400
            response.content = '参数错误'
            return response
        the_content, the_format = base64_decode.transfer(the_file)

        is_webm = request.POST.get('source')
        if is_webm == "webm":
            the_format = "webm"

        pure_name = str(datetime.datetime.now())

        fname = os.path.join(MEDA_PATH, the_format, pure_name + '.' + the_format)

        with open(fname, 'wb') as fout:
            fout.write(the_content)

        save_path = os.path.join(MEDA_PATH, 'mid', pure_name + '-pro.mid')
        print(Transfer(fname, the_style,save_path))

        response.content = GET_HEAD + "mid/" + pure_name + "-pro.mid"
        response.status_code = 200
    else:
        response.status_code = 400
        response.content = "Wrong way to get source"

    return response


