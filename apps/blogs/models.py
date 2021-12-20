
from django.db                  import models
from django.utils               import timezone
from django.utils.text          import slugify
from django.contrib.auth.models import User as AbstractBaseUser, PermissionsMixin
from ckeditor.fields            import RichTextField 
# from apps.categories.models     import Category
from apps.users.models          import User

class Category(models.Model):

    
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        db_table = 'categorias'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.PROTECT) #lo que hace el models.PROTECT es protejer a este en caso de que su "padre" sea eliminado ya que este es una clave foranea


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
        db_table = "posteos"
        ordering = ('title',)


    def __str__(self):
        
        return '{} by @{}'.format(self.title, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)