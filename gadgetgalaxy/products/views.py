from django.http import HttpResponse
from django.shortcuts import redirect, render

from category.models import Category
from products.models import Products

# Create your views here.
def product_list(request):
    products = Products.getall()
    return render(request, 'product/list.html', {'products': products})

def product_new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')
        sku = request.POST.get('sku')
        category_id = request.POST.get('category_id')

        Products.product_new(
            name=name,
            price=price,
            description=description,
            image=image,
            stock=stock,
            sku=sku,
            category_id=category_id
        )
        return redirect('product_list')
    categories = Category.objects.all()
    return render(request, 'product/new.html', {'categories': categories})


def soft_delete_product(request, id):
    Products.softdelete(id)
    return redirect('product_list')

def hard_delete_product(request, id):
    Products.harddel(id)
    return redirect('product_list')