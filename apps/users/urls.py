from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register',views.Registrarme.as_view(),name='register'),
    path('<slug:slug>', views.Profile.as_view(), name='profile'),

    # admin
    # path(),
]