from django.urls import path

from .views import PersonListView

app_name = 'app_django_tables2'
urlpatterns = [
    path('people/', PersonListView.as_view()),
]
