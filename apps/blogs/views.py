from django.views.generic.list import ListView #Crear listas de objetos
from django.views.generic.detail import DetailView #ver esas listas
from apps.blogs.models import Post

class PostList(ListView):
    model = Post
    template_name = "url.html" #aqui agregar que plantilla.html se va a mostrar
    paginate_by = 6 #Cuantos elementos va a tener cada pagina 
    context_object_name = "url" #como sera nombrada la variable en ka plantialla

    def get_queryset(self, **kwargs):
        return Post.objects.filter(presentar=True).order_by("-publicado")



class PostDetailView(DetailView): #permite ver un objeto a traves de una url

    model = Post
    template_name = 'url.html'
    context_object_name = 'url'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
