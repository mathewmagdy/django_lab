from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('New/', views.product_new, name='product_new'),
    path('delete/<int:id>/', views.hard_delete_product, name='hard_delete_product'),
    path('softdelete/<int:id>/', views.soft_delete_product, name='soft_delete_product'),
    path('Update/<int:id>/', views.update_product, name='update_product'),
]