from django.urls import path

from . import  views

urlpattern = [
    path('',views.process_audio, name="procession"),
]