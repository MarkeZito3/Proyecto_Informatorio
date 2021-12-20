
# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Models
from django.contrib.auth.models import User as user_model
from apps.users.models import User

class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre",max_length=50,widget=forms.TextInput({"placeholder":"Nombre"}))
    last_name = forms.CharField(label="Apellido",max_length=50,widget=forms.TextInput({"placeholder":"Apellido"}))
    email = forms.CharField(label="e-mail",min_length=6,max_length=70,widget=forms.EmailInput({"placeholder":"E-mail"}))
    username = forms.CharField(label="Nombre de Usuario",min_length=6,max_length=70,widget=forms.TextInput({"placeholder":"Nombre de Usuario"}))
    password1 = forms.CharField(label="Contraseña",max_length=70,widget=forms.PasswordInput({"placeholder":"Contraseña"}))
    password2 = forms.CharField(label="Confirmar Contraseña",max_length=70,widget=forms.PasswordInput({"placeholder":"Repira la contraseña"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email",]

    def clean_password(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise ValidationError("las contraseñas no coinciden")
        return password1,password2