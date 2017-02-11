from django import forms
from django.forms import Textarea
from .models import Conglomerate, Cert, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('conglomerate', 'name', 'category', 'text', 'last_updated', 'num_stars', 'certificatons',)
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }

class ConglomerateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'text', 'last_updated', 'num_stars',)
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }
