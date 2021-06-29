from jaguarete.models import Product
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Register
from jaguarete.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all().order_by('-create_on')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def prueba(request):
    return render(request, 'user.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated(): #Mensaje de autenticación
                messages.info(request, 'Hola mundoooo')
            username = form.cleaned_data['username']
            return redirect('home')
    else:
        form = Register()

    return render(request, 'register.html', {'form': form})
# def register(request):
#     if request.method == 'GET':
#         return render(
#             request, 'register.html',
#             {'form': Register}
#         )
#     elif request.method == 'POST':
#             form = Register(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login =(request, user)
#                 return redirect(reverse("home"))
#                 body={
#                     'email': form.cleaned_data['email00'],
#                     'user': form.cleaned_data['user'],
#                     'password': form.cleaned_data['password'],
#                 }

    #         message = '\n'.join(body.values())

    #         try:
    #             send_mail(message, 'alexmejia992gmail.com', ['alexmejia992gmail.com'])
    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #         return redirect ('home')

    # form = Register()
    # return render(request, 'register.html', {'form':form})
