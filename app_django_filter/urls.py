from django.urls import path
from django_filters.views import FilterView, object_filter

from .models import Product
from .views import product_list

app_name = 'app_django_filter'
urlpatterns = [
    path('list_1/', product_list),

    # шаблон по умолчанию - <app>/<model>_filter.html
    # Реализация через базовый класс и ф-ию
    path('list_2/', FilterView.as_view(model=Product)),
    path('list_3/', object_filter, {'model': Product}),
]
