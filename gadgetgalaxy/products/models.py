from django.db import models

from category.models import Category

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=200 , null=True)
    price = models.DecimalField(max_digits=10 , decimal_places=2 , null=False)
    stock = models.IntegerField(null=False)
    image = models.ImageField(upload_to='products/imgs',blank=True,null=True)
    sku = models.CharField(unique=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    

    @classmethod
    def getall(cls):
        return cls.objects.all()
    
    @classmethod
    def get_by_id(cls,id):
        return cls.objects.get(pk=id)
    
    @classmethod
    def product_new(cls, name, price, description, image, stock, sku, category_id):
        category_obj = Category.get_category_by_id(category_id)
        return cls.objects.create(
            name=name,
            price=price,
            description=description,
            image=image,
            stock=stock,
            sku=sku,
            category=category_obj
        )

    @classmethod
    def harddel(cls,id):
        return cls.objects.filter(pk=id).delete()

    @classmethod
    def softdelete(cls,id):
        Products.objects.filter(pk=id).update(stock = 0)