from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
