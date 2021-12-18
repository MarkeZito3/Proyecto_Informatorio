from django.shortcuts import render

from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Forms
from apps.users.forms import SignupForm


class SignupView(FormView):
    """Users sign up view."""

    template_name = ''
    form_class = SignupForm
    success_url = reverse_lazy('users:registerok')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

"""En template_name le pasamos la template que vamos a utilizar.
En form_class el formulario que creamos anteriormente.
success_url será la url a la que redireccionará si todo ha ido bien.
Por último utilizamos la función form_valid para guardar el usuario si todo ha salido bien."""