from django.urls import path
from . import views

App_name = 'dropzoneapp'

urlpatterns = [
    path('', views.index, name="index"),
]