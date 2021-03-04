from django.shortcuts import render

from .filters import ProductFilter
from .models import Product, Manufacturer


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'django_filter/template.html', {'filter': f})
