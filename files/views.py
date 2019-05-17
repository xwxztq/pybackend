from django.shortcuts import render

# Create your views here.

import os
import datetime
from  django.http import  HttpResponse
from django.http import FileResponse
from pybackend.settings import MEDA_PATH

def uploadHandler(request):
    if request.method == "POST":
        f1 = request.FILES['file']
        fname = os.path.join(MEDA_PATH,f1.name)
        #fname = 'static/media/car/a.png'
        print(fname)
        with open(fname, 'wb+') as pic:
            # 根据上传的流中的数据一点一点往内存中写
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse(fname)
    else:
        return HttpResponse("ERROR")

def downloadHander(request):

    if request.method == "GET":
        # field = request.GET.get('field')
        name = request.GET.get('name')
        print(name)
        filename = os.path.join(MEDA_PATH,name)
        file = open(filename, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/msword'
        response['Content-Disposition'] = 'attachment;filename=' + name
        return response
    else:
        response = HttpResponse()
        response.status_code = 400
        response.content = "Wrong way to get data"
        return response

def midi2wav(request):

    response = HttpResponse()

    if request.method == 'POST':

        the_file = request.POST.get('file')
        if the_file is None:
            response.status_code = 400
            response.content = '参数错误'
            return response
        the_content, the_format = base64_decode.transfer(the_file)

        pure_name = str(datetime.datetime.now())
        fname = os.path.join(MEDA_PATH,the_format,pure_name+'.'+the_format )
        sname = os.path.join(MEDA_PATH,'wav',pure_name+".wav")

        with open(fname,'wb') as fout:
            fout.write(the_content)


