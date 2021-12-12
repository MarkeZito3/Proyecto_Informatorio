from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import SlugField, TextField
from django.utils import timezone

class category(models.Model):
    name = models.CharField(max_length=300) 
    #CharField hace ref a los numeros y letras qe podemos escribir en un campo
    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
        
    options = [
        ('draft', 'Draft'),
        ('publised', 'Published'),
    ]
    
    
    categoria = models.ForeignKey(category, on_delete=models.PROTECT, default=1 )
    #Usamos foreignKey paravincular a un modelo
    titulo = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft' )
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-publised')

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'

#habria que hacer migraciones, a mi me tirar error
