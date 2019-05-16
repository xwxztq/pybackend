import os
import sys

from django.shortcuts import render
from django.http import HttpResponse
from climax4musics.climax import get_climax
import base64_decode




def climax(request):

    response = HttpResponse()

    print(sys.path)

    if request.method == 'POST':

        file = request.POST.get('file')
        if file is None:
            response.status_code = 400
            response.content = "Invalid parameters,please check the file key"
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

