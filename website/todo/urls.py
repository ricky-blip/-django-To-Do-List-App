from django import urls
from django.urls import path

from . import views # import file views todo

urlpatterns = [
    path('', views.index, name='index'), # path is empty, import function from views, give name = index
]