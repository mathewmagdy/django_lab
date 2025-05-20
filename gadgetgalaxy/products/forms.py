from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "Select Category"

        self.fields['image'].widget.attrs.update({'accept': 'image/*'})
