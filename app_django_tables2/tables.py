"""
sequence - указать порядок столбцов
orderable - отключить упорядочивание столбца
"""
import django_tables2 as tables

from django.utils.html import format_html

from .models import Person, Customers


class PersonTable(tables.Table):
    """Таблица пользователей"""
    name = tables.Column(
        verbose_name='Полное имя', order_by=("first_name", "family_name"))

    class Meta:
        model = Person
        sequence = ('last_name', 'first_name', 'birth_date')
        exclude = ('user',)
        # template_name = "django_tables2/bootstrap.html"
        # fields = ("name",)


class CastomerTable(tables.Table):
    """Таблица клиентов. Изменить способ изображения столбца"""
    name = tables.Column()
    description = tables.Column()

    def render_name(self, value, record):
        """Переопределение вида 1изображения столбца 'name'"""
        return format_html('<b>{} {}<b>', value, record.last_name)

    def render_count(self, value):
        """Получить доступ к зарегистрированному пользователю"""
        if self.request.user.is_authenticated():
            return value
        else:
            return '-----'

    class Meta:
        model = Customers


class SimpleTable(tables.Table):
    name = tables.Column(
        attrs={
            "th": {"id": "foo"}
        })
    actions = tables.Column(orderable=False)

    class Meta:
        model = Customers


##############################################################################

class PersonColumn(tables.Column):
    attrs = {
        "td": {
            "data-first-name": lambda record: record.first_name,
            "data-last-name": lambda record: record.last_name,
        }
    }

    def render(self, record):
        return "{} {}".format(record.first_name, record.last_name)


class Table(tables.Table):
    # person = tables.Column(
    #     attrs={
    #         'td': {
    #             'data-length': lambda value: len(value)
    #         }
    #     })
    person = PersonColumn()

    class Meta:
        model = Person


##############################################################################
data = [
    {'name': 'Bradley'},
    {'name': 'Stevie'},
]


class NameTable(tables.Table):
    """Таблица через список диктов"""
    name = tables.Column()


tables = NameTable(data)
