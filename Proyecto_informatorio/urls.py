from django.contrib      import admin
from django.contrib.auth import views as auth_views
from django.urls         import path
from django.conf.urls    import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import re_path
from django.views.static import serve
# from django.views.generic import TemplateView

from . import views
from apps.blogs.views import CreatePost

urlpatterns = [
    path('admin/', admin.site.urls),
    #vistas basadas en clases
    path('', views.Index.as_view(), name='index'),
    path('services', views.Services.as_view(), name='services'), 
    path('contact', auth_views.LoginView.as_view(template_name = 'pages/contact.html'), name='contact'),
    path('logout', auth_views.logout_then_login, name="logout"), 
    
    path('users/', include('apps.users.urls')),
    path('blogs/', include('apps.blogs.urls')),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)