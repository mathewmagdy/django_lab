from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('add/', CategoryCreateView.as_view(), name='category_add'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
