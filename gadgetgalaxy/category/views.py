from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category/form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category/form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/confirm_delete.html'
    success_url = reverse_lazy('category_list')
