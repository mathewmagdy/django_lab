# from django.urls import path
# from . import views

# urlpatterns = [
#     path('list/', views.product_list, name='api_product_list'),
#     path('add/', views.add_product, name='api_add_product'),
#     path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='api_update_product'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
