from django import forms
from .models import Conglomerate, Cert, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('conglomerate', 'name', 'category', 'text', 'last_updated', 'num_stars', 'certificatons',)
