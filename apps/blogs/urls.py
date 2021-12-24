"""Posts URLs."""

# Django
from django.urls import path

# Views
from apps.blogs import views

app_name='blogs'

urlpatterns = [
    path('',views.PostsFeedView.as_view(),name='blogs'),
    # path('post/<slug:url>/save_comment',views.save_comment(),name='save_comment'),
    path('post/<slug:url>',views.PostDetailView.as_view(),name='detail'),
    path('create',views.CreatePost.as_view(),name='create'),
]