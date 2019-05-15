from django.shortcuts import render
import os
from django.http import FileResponse, HttpResponse
from pybackend.settings import MEDA_PATH
import music21
from binascii import a2b_base64
import base64


# Create your views here.

def transfer(request):

    print(request.method,"RRRRRRRRRRRRRRRRRRRRRRResquest")
    if request.method == "POST":
        f1 = request.POST.get('file')
        

        tmpfile = open("tmpfile","w")
        tmpfile.write(f1)
        print(f1)
        fname = os.path.join(MEDA_PATH, "mid", "justtmp.mid")
        # purename = f1.name.split('.')
        # fname = 'static/media/car/a.png'
        print("This is filepath",fname)
        missing_padding =  4 - len(f1)%4
        print(missing_padding)
        if missing_padding:
            f1 += '='*missing_padding
        print(len(f1))
        print("123132133212131",len(f2))

        with open(fname, 'wb') as pic:
            # 根据上传的流中的数据一点一点往内存中写
                pic.write(base64.b64decode(f1))
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




