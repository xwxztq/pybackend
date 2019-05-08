from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from wav2mids.w2m import wav2mid


def get_wav2mid(request):
    response = HttpResponse()

    if request.method == 'POST':

        filepath = request.POST.get('filepath', "")
        save_path = request.POST.get('savepath', "")

        if filepath == "":
            response.status_code = 400
            response.content = "params wrong"

        else:

            # todo: check file exists

            if save_path == "":

                # todo check the path is leagel
                result = wav2mid.transfer(filepath)

            else:

                # todo check the path is leagel
                result = wav2mid.transfer(filepath, save_path)

            response.status_code = 200
            response.content = result

    else:
        return HttpResponse('获取资源方式错误')

