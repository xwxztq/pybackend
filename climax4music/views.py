from django.shortcuts import render
from django.http import HttpResponse

def climax(request):

    if request.method == 'POST':

        filepath = request.POST.get('filepath',"")

        if filepath == "":
            return HttpResponse("参数错误")
        else:
            return HttpResponse(filepath)

    else:
        return HttpResponse('获取资源方式错误')


