#debemos declarar la vista que queremos mostrar
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    #hace referencia a lo que queres cargar cuando carguemos la clase
    template_name = 'index.html'