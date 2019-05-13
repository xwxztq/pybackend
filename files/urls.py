from django.urls import path
from . import  views

urlpatterns = [
    path('upload',views.uploadHandler),
    path('download',views.downloadHander),
]