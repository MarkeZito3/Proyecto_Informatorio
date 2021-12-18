
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from apps.users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )


    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
"""Aquí lo que estamos haciendo es declarar la clase SignupForm que contendrá todos los
 campos de nuestro formulario, en este caso estamos declarando que todos los campos sean
  de tipo texto. Con el campo widget declaramos el sub tipo, para el email, será un input
   mail, username de tipo input text, y para las contraseñas de tipo password.

Después declaramos la función clean que se ejecutará después de enviar el formulario y
 validará si la contraseña es igual a la constraseña repetida.

Para finalizar creamos la función save que lo que hará será elminar el campo 
password_confirmation y guardará la información enviada en la tabla User y Profile."""