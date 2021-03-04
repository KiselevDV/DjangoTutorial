from django_tables2 import SingleTableView

from django.shortcuts import render
from django.views.generic import ListView

from .models import Person
from .tables import PersonTable


class PersonListView(ListView):
    model = Person
    template_name = 'app_django_tables2/people.html'


class NewPersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'app_django_tables2/people.html'
