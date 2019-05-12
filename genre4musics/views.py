from django.shortcuts import render

# Create your views here.

import os
from django.http import  HttpResponse


def get_genre(request):

    response = HttpResponse()

    if request.method == 'POST':

        pass

    else:

        response.status_code = 400
        response.content = "Wrong way to get source"

    return response

