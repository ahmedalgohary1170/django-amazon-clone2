from django.shortcuts import render


from .models import Products,Brand,Reviews

from django.views.generic import ListView,DetailView



class ProductList(ListView):
    model = Products


class ProductDetail(DetailView):
    model = Products
