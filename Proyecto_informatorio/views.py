from django.shortcuts import render
from django.views.generic import TemplateView

#views basadas en clases 
"""
    todos estos se encuentran en django.views.generic

    DetaileView: solo muestra un valor de la base de datos
    ListView: listar todos los objetos de un modelo particular
    CreateView: crea un objeto
    UpdateView: actualiza un objeto
    DelateView: borra un objeto
    TemplateView: solamente muestra un template

    estas son unas vistas que ya estan en django que ya tienen todo el código necesario
    para la cumplir con esas funcionalidades
"""

class Index(TemplateView):
    template_name = "index.html"

class Services(TemplateView):
    template_name = "pages/services.html"

class Blog(TemplateView):
    template_name = "pages/blog.html"

class Passwordrequest(TemplateView):
    template_name = "pages/passwordrequest.html"

class Profile(TemplateView):
    template_name = "pages/profile.html"

class Blog__Single(TemplateView):
    template_name = "pages/blog-single.html"

#views basadas en funciones

