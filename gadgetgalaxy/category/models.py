from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)

    @classmethod
    def get_category_by_id(cls, category_id):
        return cls.objects.get(pk=category_id)
    
    def __str__(self):
        return self.name
