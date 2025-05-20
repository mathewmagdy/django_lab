from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from category.models import Category
from products.models import Products

from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Products.getall()
    return render(request, 'product/list.html', {'products': products})

# def product_new(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
#         stock = request.POST.get('stock')
#         sku = request.POST.get('sku')
#         category_id = request.POST.get('category_id')

#         Products.product_new(
#             name=name,
#             price=price,
#             description=description,
#             image=image,
#             stock=stock,
#             sku=sku,
#             category_id=category_id
#         )
#         return redirect('product_list')
#     categories = Category.objects.all()
#     return render(request, 'product/new.html', {'categories': categories})



def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/new2.html', {'form': form})


def soft_delete_product(request, id):
    Products.softdelete(id)
    return redirect('product_list')

def hard_delete_product(request, id):
    Products.harddel(id)
    return redirect('product_list')

# def update_product(request, id):
#     product = get_object_or_404(Products, pk=id)
#     categories = Category.objects.all()

#     if request.method == 'POST':
#         product.name = request.POST.get('name')
#         product.price = request.POST.get('price')
#         product.description = request.POST.get('description')
#         product.stock = request.POST.get('stock')
#         product.sku = request.POST.get('sku')
#         product.category_id = request.POST.get('category_id')

#         # Handle optional image update
#         image = request.FILES.get('image')
#         if image:
#             product.image = image

#         product.save()
#         return redirect('product_list')

#     return render(request, 'product/update.html', {'product': product, 'categories': categories})

def product_update(request, pk):
    product = get_object_or_404(Products, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/update2.html', {'form': form, 'product': product})