from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# from django.contrib.auth.models import User as user_model #provee los campos para crear la tabla
from django.db import models


# class Profile(models.Model):

#     user = models.OneToOneField("users.User", on_delete=models.CASCADE)

#     website = models.URLField(max_length=200, blank=True)

#     photo = models.ImageField(
#         upload_to='users/pictures',
#         blank=True,
#         null=True
#     )

#     date_modified = models.DateTimeField(auto_now=True)

# # añadir la opción de que el usuario pueda guardar su website, añadir una foto y la fecha de modificación del usuario.
#     def __str__(self):
#         return self.user.username

class User(AbstractUser):
    slug = models.SlugField(unique=True)
    es_writer = models.BooleanField(default=False)
    es_comment = models.BooleanField(default=True)
    es_administrador = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    
    class Meta:
        db_table = 'usuarios'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"