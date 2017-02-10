from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import inlineformset_factory

from .models import Conglomerate, Product, Cert


def index(request):
    return render(request, 'thesite/index.html', {})

def the_story(request):
    return render(request, 'thesite/the_story.html', {})

@login_required
def submit(request):
    return render(request, 'thesite/submit.html', {})

"""
@login_required
def submit(request):
    ProductInlineFormSet = inlineformset_factory(Product, Conglomerate, Cert, fields=('name',))  # From where are the fields?
    if request.method == "POST":
        formset = ProductInlineFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(reverse('thesite/submit.html'))
    else:
        formset = ProductInlineFormSet()
    return render(request, 'thesite/submit.html', {'formset': formset})

"""

def database(request):
    conglom = Conglomerate.objects.all()
    products = Product.objects.all()
    return render(request, 'thesite/database.html', {'conglom':conglom, 'products': products,},)

"""
def modify_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'thesite/modify_product.html', {'product':product})
"""

@login_required
def modify_product(request, pk):
    conglomerate = Conglomerate.objects.get(pk=pk)
    ConglomerateInlineFormSet = inlineformset_factory(Conglomerate, Product,   fields=('name','category','text',))  # From where are the fields?
    if request.method == "POST":
        formset = ConglomerateInlineFormSet(request.POST, request.FILES, instance=conglomerate)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(reverse('thesite/database.html'))
    else:
        formset = ConglomerateInlineFormSet(instance=conglomerate)
    return render(request, 'thesite/modify_product.html', {'formset': formset})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
