from django.urls import path
from jaguarete import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('prueba/', views.prueba, name='prueba'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name= 'contact'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('login/', LoginView.as_view('views.login'), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
