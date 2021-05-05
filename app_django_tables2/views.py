from django.shortcuts import render
from django_tables2 import SingleTableView

from .models import Person, Customers
from .tables import PersonTable, CastomerTable, SimpleTable, Table


class PersonListView(SingleTableView):
    """Все лица"""
    model = Person
    table_class = PersonTable
    template_name = 'app_django_tables2/people.html'


def person_list(request):
    """Все лица"""
    table = PersonTable(Person.objects.all())
    context = {
        'table': table,
    }
    return render(request, 'person_list.html', context)
