from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path('blog', views.PostDetailView.as_view(), name='blog'),
    # path('create/', ),
]