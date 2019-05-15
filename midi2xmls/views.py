from django.shortcuts import render
import os
from django.http import FileResponse, HttpResponse
from pybackend.settings import MEDA_PATH
import music21
from binascii import a2b_base64
import base64
import datetime
import re


def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


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

        content = content.split(',')[1]

        ori_image_data = decode_base64(content.encode())

        pure_name = str(datetime.datetime.now())

        fname = os.path.join(MEDA_PATH, "mid", pure_name+".mid")

        with open(fname, 'wb') as fout:
            fout.write(ori_image_data)


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
