from django.shortcuts import render
import os
from django.http import FileResponse, HttpResponse
from pybackend.settings import MEDA_PATH
import music21


# Create your views here.

def transfer(request):
    if request.method == "POST":
        f1 = request.FILES['file']
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
        mid_path = os.path.join(MEDA_PATH, "mid", purename[0], ".mid")
        try:
            ext.write('xml',fp=mid_path)
        except:
            response = HttpResponse()
            response.status_code = 500
            response.content = "xml文件写入时出错"
        else:
            with open(mid_path,"rb+") as ret:
                response = FileResponse(ret)
                response['Content-Type'] = 'application/msword'
                response['Content-Disposition'] = 'attachment;filename=' + purename[0]+".mid"
    else:
        response = HttpResponse("HTTP请求错误")
        response.status_code = 400

    return response




