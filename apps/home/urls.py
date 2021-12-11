from django.urls import path
from .views import (
    BlogHomePageView,
    PostDetailView,
)

app_name= 'blog'

urlpatterns= [
    path('', BlogHomePageView.as_view(), name='home'),
    path('<slug:<slug>/', PostDetailView.as_view(), name='post-detail'),
]