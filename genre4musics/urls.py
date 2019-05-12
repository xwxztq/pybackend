from django.urls import path

from . import views

urlpattern = [
    path('',views.get_genre,name='genre'),
]