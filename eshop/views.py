from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from eshop.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'price'
    ]
    success_url = reverse_lazy('list_view')


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'price'
    ]
    success_url = reverse_lazy('list_view')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list_view')
