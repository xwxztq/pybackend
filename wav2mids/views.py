from django.shortcuts import render

# Create your views here.
import os
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
                save_path = os.path.split(filepath)
                # todo check the path is leagel


            else:

                # todo check the path is leagel
                pass
            result = wav2mid.transfer(filepath,save_path)

            response.status_code = 200
            response.content = result

    else:
        response.status_code = 400
        response.content = "Wrong way to get source"

    return response

