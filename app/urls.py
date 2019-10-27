from django.urls import path

from . import views

urlpatterns = [
    path('', views.valuebase, name='valuebase')
]

