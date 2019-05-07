from django.shortcuts import render
from django.http import HttpResponse
from climax4musics.climax import get_climax

def climax(request):

    if request.method == 'POST':

        filepath = request.POST.get('filepath',"")

        if filepath == "":
            return HttpResponse("参数错误")
        else:
            return HttpResponse( get_climax(filepath) )

    else:
        return HttpResponse('获取资源方式错误')


