"""Posts URLs."""

# Django
from django.urls import path

# Views
from apps.blogs import views
app_name='blogs'
urlpatterns = [

  
    path('post/<slug:url>',views.PostDetailView.as_view(),name='detail'),
]

 