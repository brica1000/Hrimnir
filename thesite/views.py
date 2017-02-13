from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import inlineformset_factory

from .models import Conglomerate, Product, Cert
from thesite.forms import ProductForm, ConglomerateForm, VerificationForm, VerificationConglomForm

from modules.mymodule import helpers


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

"""
@login_required
def modify_conglomerate(request, pk):
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
    return render(request, 'thesite/modify_conglomerate.html', {'formset': formset})
"""
def view_conglomerate(request, pk):
    conglomerate = get_object_or_404(Conglomerate, pk=pk)
    products = conglomerate.product_set.all()
    return render(request, 'thesite/view_conglomerate.html', {'conglomerate': conglomerate, 'products':products,})

@login_required
def modify_conglomerate(request, pk):
    conglomerate = get_object_or_404(Conglomerate, pk=pk)
    products = conglomerate.product_set.all()
    if request.method == "POST":
        form = ConglomerateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('database'))
    else:
        form = ConglomerateForm(instance=conglomerate)
    return render(request, 'thesite/modify_conglomerate.html', {'conglomerate': conglomerate,'form': form, 'products':products,})

def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    verifications = product.verification_set.all()
    return render(request, 'thesite/view_product.html', {'product':product, 'verifications': verifications})

@login_required
def modify_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('database'))
    else:
        form = ProductForm(instance=product)
    return render(request, 'thesite/modify_product.html', {'form': form,})

@login_required
def submit_verification(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = VerificationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('database'))
    else:
        form = VerificationForm(initial={'product': product, 'conglomerate': product.conglomerate})
    return render(request, 'thesite/submit_verification.html', {'form': form, 'product': product})

@login_required
def submit_verification_conglom(request, pk):
    conglomerate = get_object_or_404(Conglomerate, pk=pk)
    if request.method == "POST":
        form = VerificationConglomForm(request.POST)
        form.fields['comment'].required = False
        form.fields['comment_employ'].required = False
        form.fields['comment_sustain'].required = False
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('database'))
    else:
        form = VerificationConglomForm(initial={'conglomerate': conglomerate})
    return render(request, 'thesite/submit_verification_conglom.html', {'form': form, 'conglomerate':conglomerate})

@login_required
def compare_edits(request):
    data = { 'products': Product.objects.all(), 'conglomerates': Conglomerate.objects.all(),'info' : [],
             'message_0': "Nothing choosen", 'message_1': "", 'style': "", 'l_left': "", 'l_right': "",
             'zipped': "", 'zipped_repeat': ""}
    if request.POST.get('action_1', False) == "checkboxes":  # old: request.method == "POST"
        info=request.POST.getlist("checkbox")  # This is a list of the strings from the corr. checkbox values
        info = [ int(x) for x in info ] # We need int format to keep checkboxes checked, it won't affect what's below
        if len(info) == 2:  # Make sure only two are selected!
            (message_0, message_1) = helpers.new_old_color(info)
            (style, l_left, l_right) = helpers.compare_fields(message_0, message_1)
            data['info'] = info
            data['message_0'] = message_0
            data['message_1'] = message_1
            data['zipped'] = zip(style, l_left, l_right)
            data['zipped_repeat'] = zip(style, l_left, l_right)
            if isinstance(message_1, Product):  # Use modifty product form, note we only check one of the checked items hoping that they are of the same class
                product = get_object_or_404(Product, pk=message_1.pk)
                print(request.POST.get('action_2', 'action_1') == "form-submit")
                if request.POST.get('action_2', 'action_1') == "form-submit":
                    form = ProductForm(request.POST)
                    if form.is_valid():
                        form.save()
                        data['form'] = form
                        print('flaag')
                        return HttpResponseRedirect(reverse('database'))
                    else:
                        print('flag')
                else:
                    form = ProductForm(instance=product)
                    data['form'] = form
                return render(request, 'thesite/compare_edits.html', data)

        else:
            data['message_0'] = "Choose two boxes please"
    else:
        data = data
    return render(request, 'thesite/compare_edits.html', data)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
