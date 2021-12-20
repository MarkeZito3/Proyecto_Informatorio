"""User forms."""

# Django
from django import forms

# Models
from apps.comments.models import Comment
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):
    """Post model form."""

    comment = forms.CharField(widget=forms.Textarea)


    class Meta:
        """Form settings."""

        model = Comment
        fields = ('user', 'post', 'comment')

"""Aquí estamos creando un campo de tipo textarea que será el que guarde el comentario 
del usuario y en la clase Meta le decimos el modelo de referencia y los campos que tiene
 que guardar, en este caso el usuario que lo ha escrito, el post al que va referenciado 
 y el comentario."""