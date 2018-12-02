from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.index, name='index'),
    path('', views.login, name='login'),
]