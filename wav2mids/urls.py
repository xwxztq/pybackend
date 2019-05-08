from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_wav2mid, name = 'wav2mid'),
]
