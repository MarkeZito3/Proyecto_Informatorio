"""Posts URLs."""

# Django
from django.urls import path

# Views
from apps.blogs import views

urlpatterns = [

  
    path(
        route='posts/<slug:url>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),

   """ path(
        route='posts/save_comment',
        view=views.save_comment,
        name='save_comment'
    ),"""

]

 