# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from django.views.generic.edit import UpdateView
# from django.forms.models import model_to_dict
# from products.models import Products
# from products.forms import ProductForm

# #Function-based views

# def product_list(request):
#     products = Products.objects.all().values()
#     return JsonResponse(list(products), safe=False)

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             return JsonResponse(model_to_dict(product), status=201)
#         return JsonResponse(form.errors, status=400)
#     return JsonResponse({'detail': 'Method not allowed'}, status=405)


# #Class-based view for Update

# class ProductUpdateView(UpdateView):
#     model = Products
#     form_class = ProductForm

#     def form_valid(self, form):
#         self.object = form.save()
#         return JsonResponse(model_to_dict(self.object))

#     def form_invalid(self, form):
#         return JsonResponse(form.errors, status=400)


# from rest_framework.generics import UpdateAPIView , RetrieveAPIView ,DestroyAPIView
# from products.models import Products
# from products.api.serializers import ProductSerializer



# class ProductUpdateView(UpdateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'


# class ProductDetailView(RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'

# class ProductDeleteView(DestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'



from rest_framework import viewsets
from products.models import Products
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
