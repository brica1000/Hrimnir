from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import inlineformset_factory

from .models import Conglomerate, Product, Cert
from thesite.forms import ProductForm


def index(request):
    return render(request, 'thesite/index.html', {})

def the_story(request):
    return render(request, 'thesite/the_story.html', {})

@login_required
def submit(request):
    return render(request, 'thesite/submit.html', {})


def database(request):
    conglom = Conglomerate.objects.all()
    products = Product.objects.all()
    return render(request, 'thesite/database.html', {'conglom':conglom, 'products': products,},)

@login_required
def modify_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('database'))
    else:
        form = ProductForm(instance=product)
    return render(request, 'thesite/modify_product.html', {'form': form,})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
