from django.contrib.auth import authenticate, login
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import NewProductForm, RegisterForm
from jaguarete.models import Product


from django.conf import settings
from importlib import import_module

class Home(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-create_on')

def about(request):
    return render(request, 'about.html', {})

def new_product(request):
    form = NewProductForm()
    if request.method == 'POST':
        # print('Printing', request.POST)
        form = NewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('no es valido')
    context ={'form': form}
    return render(request, 'new_product.html', context)

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'new_product.html'
    form_class = NewProductForm
    success_url = reverse_lazy('home')
    
class ViewProduct(DetailView):
    model = Product
    template_name = 'view_product.html'
    context_object_name = 'product'

def contact(request):
    return render(request, 'contact.html', {})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        searched_category = Product.objects.filter(Q(product_name__contains=searched) |
        Q(category__category_name__contains=searched))
        return render(request, 'search.html', {'searched': searched, 'searched_category': searched_category})
    else:
        return render(request, 'search.html', {})

def cart(request):
    return render(request, 'cart.html', {})


