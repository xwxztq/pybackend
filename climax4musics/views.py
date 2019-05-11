import os
import sys

from django.shortcuts import render
from django.http import HttpResponse
from climax4musics.climax import get_climax

def climax(request):

    response = HttpResponse()

    cur_pwd = os.getcwd()
    if cur_pwd in sys.path:
        pass
    else:
        sys.path.append(cur_pwd+"climax")

    print(sys.path)

    if request.method == 'POST':

        filepath = request.POST.get('filepath',"")

        if filepath == "":
            response.status_code = 400
            response.content = "Parameters \'filepath\' is empty"
        else:
            response.status_code = 200
            response.content = str(get_climax.process_audio(filepath))

    else:
        response.status_code = 400
        response.content = "获取资源方式错误"

    return response

