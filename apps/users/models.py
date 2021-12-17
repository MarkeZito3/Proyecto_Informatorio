"""from django.contrib.auth.models import User #provee los campos para crear la tabla
from django.db import models


class Profile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    website = models.URLField(max_length=200, blank=True)

    photo = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    date_modified = models.DateTimeField(auto_now=True)

# añadir la opción de que el usuario pueda guardar su website, añadir una foto y la fecha de modificación del usuario.
    def __str__(self):
        return self.user.username"""

