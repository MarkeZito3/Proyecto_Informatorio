from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),


    #vistas basadas en clases
    path('', views.Index.as_view(template_name='index.html'), name='index'),
    path('services', views.Services.as_view(template_name='pages/services.html'), name='services'),
    path('blog',views.Blog.as_view(template_name='pages/blog.html'),name='blog'),
    path('contact', views.Contact.as_view(template_name='pages/contact.html'), name='contact'),
    path('registro', views.Register.as_view(template_name='pages/registro.html'), name='register'),
    path('passwordrequest', views.Passwordrequest.as_view(template_name='pages/passwordrequest.html'), name='passwordrequest'),
]