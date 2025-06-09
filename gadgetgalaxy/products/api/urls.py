from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name='api_product_list'),
    path('add/', views.add_product, name='api_add_product'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='api_update_product'),
]
