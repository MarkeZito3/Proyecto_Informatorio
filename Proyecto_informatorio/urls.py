from django.contrib      import admin
from django.contrib.auth import views as auth_views
from django.urls         import path
from django.conf.urls    import url, include
# from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #vistas basadas en clases
    path('', views.Index.as_view(), name='index'),
    path('services', views.Services.as_view(), name='services'),
    path('blog',views.Blog.as_view(),name='blog'),
    path('registro', views.Register.as_view(), name='register'),
    path('passwordrequest', views.Passwordrequest.as_view(), name='passwordrequest'),
    path('contact', auth_views.LoginView.as_view(template_name = 'pages/contact.html'), name='contact'),
    path('logout', auth_views.logout_then_login, name="logout"),
    path('profile', views.Profile.as_view(), name='profile'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
   
]