from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.utils.regex_helper import next_char
from jaguarete import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('new_product/', views.new_product, name='new_product'),
    path('view_product/<int:pk>/', views.ViewProduct.as_view(), name='view_product'),
    path('update_product/<int:pk>', views.UpdateProduct.as_view(), name='update_product' ),
    path('cart/', views.cart, name='cart'),
    # path('add_to_cart/', views.Cart.add, name=('add_to_cart')),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name= 'contact'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('search/', views.search, name='search'),

    # path('update_item/', views.updateItem, name='update_item')
    # path('login/', LoginView.as_view('views.login'), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
