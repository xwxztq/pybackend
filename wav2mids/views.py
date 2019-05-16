from django.shortcuts import render

# Create your views here.
import os
from django.http import HttpResponse
from wav2mids.w2m import wav2mid
from pybackend.settings import MEDA_PATH,GET_HEAD
import base64_decode
import datetime

def get_wav2mid(request):
    response = HttpResponse()

    if request.method == 'POST':

       the_file = request.POST.get('file')
       if the_file is None:
           response.status_code = 400
           response.content = '参数错误'
           return  response
       the_content,the_format = base64_decode.transfer(the_file)

       pure_name = str(datetime.datetime.now())

       fname = os.path.join(MEDA_PATH,the_format,pure_name+'.'+the_format)

       with open(fname, 'wb') as fout:
           fout.write(the_content)

       save_path = os.path.join(MEDA_PATH,'mid',pure_name+'-pred.mid')
       print(wav2mid.transfer(fname,save_path))


       response.content =GET_HEAD + "mid/" +pure_name +"-pred.mid"
       response.status_code = 200

    else:
        response.status_code = 400
        response.content = "Wrong way to get source"

    return response
