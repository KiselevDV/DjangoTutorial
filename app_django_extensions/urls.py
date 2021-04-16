from django.urls import path

from . import views

app_name = 'app_django_extensions'
urlpatterns = [
    path('', views.index, name='index'),
]
