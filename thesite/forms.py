from django import forms
from django.forms import Textarea
from .models import Conglomerate, Cert, Product, Verification


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('conglomerate', 'name', 'category', 'text', 'sustainability', 'employees', 'num_stars', 'certificatons',)
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'sustainability': forms.fields.TextInput(attrs={'size': 400,}),
            'sustainability': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'employees': forms.fields.TextInput(attrs={'size': 400,}),
            'employees': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }


class ConglomerateForm(forms.ModelForm):

    class Meta:
        model = Conglomerate
        fields = ('name', 'category', 'text', 'sustainability', 'employees', 'num_stars',)
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'sustainability': forms.fields.TextInput(attrs={'size': 400,}),
            'sustainability': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'employees': forms.fields.TextInput(attrs={'size': 400,}),
            'employees': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }


class VerificationForm(forms.ModelForm):

    class Meta:
        model = Verification
        fields = ('product', 'conglomerate', 'individual', 'comment', 'who')

class VerificationConglomForm(forms.ModelForm):

    class Meta:
        model = Verification
        fields = ('conglomerate', 'individual', 'comment', 'comment_sustain', 'comment_employ', 'who')

class CompareProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('conglomerate', 'name', 'category', 'text', 'sustainability', 'employees', 'num_stars',
                  'certificatons', 'approved_edit')
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'sustainability': forms.fields.TextInput(attrs={'size': 400,}),
            'sustainability': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'employees': forms.fields.TextInput(attrs={'size': 400,}),
            'employees': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }


class CompareConglomerateForm(forms.ModelForm):

    class Meta:
        model = Conglomerate
        fields = ('name', 'category', 'text', 'sustainability', 'employees', 'num_stars', 'approved_edit')
        widgets = {
            'text': forms.fields.TextInput(attrs={'size': 400,}),
            'text': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'sustainability': forms.fields.TextInput(attrs={'size': 400,}),
            'sustainability': Textarea(attrs={'rows': 10, 'cols': 100, }),
            'employees': forms.fields.TextInput(attrs={'size': 400,}),
            'employees': Textarea(attrs={'rows': 10, 'cols': 100, }),
        }
