from django.urls import path

from . import views

urlpatterns = [
    path('register',views.Registrarme.as_view(),name='register'),
]