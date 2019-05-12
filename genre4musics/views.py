from django.shortcuts import render

# Create your views here.

import os
from django.http import  HttpResponse
from .genres import run


def get_genre(request):

    response = HttpResponse()

    if request.method == 'POST':

        filepath = request.POST.get('filepath',"")

        try:
            response.status_code = 200
            response.content= run.calculate(filepath)
        except:
            response.status_code = 500
            response.content = "Server Error"


    else:

        response.status_code = 400
        response.content = "Wrong way to get source"

    return response

