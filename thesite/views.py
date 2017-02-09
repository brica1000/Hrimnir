from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Conglomerate, Product


def index(request):
    return render(request, 'thesite/index.html', {})

def the_story(request):
    return render(request, 'thesite/the_story.html', {})

def submit(request):
    return render(request, 'thesite/submit.html', {})

def database(request):
    conglom = Conglomerate.objects.all()
    products = Product.objects.all()
    return render(request, 'thesite/database.html', {'conglom':conglom, 'products': products,},)

def modify_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'thesite/modify_product.html', {'product':product})
