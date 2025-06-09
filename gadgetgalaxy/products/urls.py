from django.urls import include, path
from django.contrib import admin
from . import views
from .views import ProductDeleteView, ProductListView

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    # path('', ProductListView.as_view(), name='product_list'),
    # path('New/', views.product_new, name='product_new'),
    # path('delete/<int:id>/', views.hard_delete_product, name='hard_delete_product'),
    # path('softdelete/<int:id>/', views.soft_delete_product, name='soft_delete_product'),
    # path('Update/<int:pk>/', views.product_update, name='product_update'),
    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # path('api/products/', include('products.api.urls')),
    path('admin/', admin.site.urls),
    path('api/products/', include('products.api.urls')), 
]