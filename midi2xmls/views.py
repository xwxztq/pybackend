from django.shortcuts import render
import os
from django.http import FileResponse, HttpResponse
from pybackend.settings import MEDA_PATH
import music21


# Create your views here.

def transfer(request):

    print(request.method,"RRRRRRRRRRRRRRRRRRRRRRResquest")
    if request.method == "POST":
        f1 = request.FILES.get('file')
        print(len(f1))
        fname = os.path.join(MEDA_PATH, "mid", f1.name)
        purename = f1.name.split('.')
        # fname = 'static/media/car/a.png'
        print(fname)
        with open(fname, 'wb+') as pic:
            # 根据上传的流中的数据一点一点往内存中写
            for c in f1.chunks():
                pic.write(c)
        score = music21.converter.parse(fname)
        ext = music21.stream.Stream(score)
        xml_path = os.path.join(MEDA_PATH, "xml", purename[0]+".xml")
        ret_path = "http://47.99.83.172/files/download?name=xml/"+purename[0]+".xml"
        ext.write('xml',fp=xml_path)
        response = HttpResponse()
        response.content = ret_path
        response.status_code =200
        # ret = open(xml_path,"rb")
        # response = FileResponse(ret)
        # response['Content-Type'] = 'application/msword'
        # response['Content-Disposition'] = 'attachment;filename=' + purename[0]+".xml"
    elif request.method == "OPTIONS":
        response = HttpResponse()
        response.response['Access-Control-Allow-Method'] = "POST"
        response['Access-Control-Allow-Origin'] = "*"
        response.status_code = 200
        print ("HHHHHHHHHHHHHHHHHHHHHHHHere I am")
        return response
    else:
        response = HttpResponse("HTTP请求错误")
        response.status_code = 400

    return response




