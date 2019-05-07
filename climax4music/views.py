from django.shortcuts import render
from django.http import HttpResponse
from . import climax4music.get_climax

def climax(request):

    if request.method == 'POST':

        filepath = request.POST.get('filepath',"")

        if filepath == "":
            return HttpResponse("参数错误")
        else:
            res = climax4music.get_climax(cfilepath)
            return HttpResponse(res)

    else:
        return HttpResponse('获取资源方式错误')


