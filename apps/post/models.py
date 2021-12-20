
"""from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField #Editor de texto/hay que instalarlo
from categories.models import Category

class Post(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to='posts/photos')#Cabecera del post
    post = RichTextField()#permite crer textos con distintos tamaños, tipos de letra, colores, etc

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)#Un campo de tipo booleano, guardaremos si es un borrador o lo queremos mostrar en la web.
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category) # El listado de categorías asignadas a un post, es una relación de tipo N a N ya que un post puede tener varias categorías y una categoría puede pertenecer a varios posts.

    class Meta:
        ordering = ('title',)


    def __str__(self):
        
        return '{} by @{}'.format(self.title, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)"""