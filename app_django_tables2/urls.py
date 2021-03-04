from django.urls import path

from .views import PersonListView, NewPersonListView

app_name = 'app_django_tables2'
urlpatterns = [
    path('people/', PersonListView.as_view()),
    path('people/', NewPersonListView.as_view()),
]
