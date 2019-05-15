from django.shortcuts import render
import os
from django.http import FileResponse, HttpResponse
from pybackend.settings import MEDA_PATH
import music21
from binascii import a2b_base64
import datetime
import base64_decode



def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = decode_base64(base64_data.encode())
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()


# Create your views here.

def transfer(request):
    print(request.method, "RRRRRRRRRRRRRRRRRRRRRRResquest")
    if request.method == "POST":
        content = request.POST.get('file')
        print(content)

        the_content ,the_format= base64_decode.transfer(content)
        print(the_format)

        if the_format != 'mid':
            response = HttpResponse()
            response.status_code = 400
            response.content = "格式不正确"

        else:
            pure_name = str(datetime.datetime.now())

            fname = os.path.join(MEDA_PATH, "mid", pure_name+'.'+the_format)

            with open(fname, 'wb') as fout:
                fout.write(the_content)


            score = music21.converter.parse(fname)
            ext = music21.stream.Stream(score)
            xml_path = os.path.join(MEDA_PATH, "xml", pure_name+".xml")
            ret_path = "http://47.99.83.172/files/download?name=xml/" + pure_name+".xml"
            ext.write('xml', fp=xml_path)
            response = HttpResponse()
            response.content = ret_path
            response.status_code = 200
            # ret = open(xml_path,"rb")
            # response = FileResponse(ret)
            # response['Content-Type'] = 'application/msword'
            # response['Content-Disposition'] = 'attachment;filename=' + purename[0]+".xml"
    elif request.method == "OPTIONS":
        response = HttpResponse()
        response['Access-Control-Allow-Method'] = "POST"
        response['Access-Control-Allow-Origin'] = "*"
        response.status_code = 200
        print("HHHHHHHHHHHHHHHHHHHHHHHHere I am")
        return response
    else:
        response = HttpResponse("HTTP请求错误")
        response.status_code = 400

    return response
