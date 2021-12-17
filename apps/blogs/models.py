"""#Django a partir de clases genera tablas para la base de datos 

from django.db import models
from django.contrib.auth.models import User #Se importa el modelo que hace referencia a los usuarios definidio por django
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return '%s' % self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    cuerpo = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)
    presentar = models.BooleanField(blank = True, null = False, default=True)
    autor = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.titulo
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)"""

#Dejo comentado por ahora 