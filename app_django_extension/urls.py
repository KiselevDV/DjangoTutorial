from django.urls import path

from . import views

app_name = 'app_django_extension'
urlpatterns = [
    path('', views.index, name='index'),
]
