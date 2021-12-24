from django                 import forms
from apps.blogs.models      import Post
# from django_quill           import forms as quill_forms 

class TextoErriquesido(forms.ModelForm):
    title = forms.CharField(label="Título",max_length=255)
    image_header = forms.IntegerField(label="Imagen de posteo")
    post = forms.TextInput()
    is_draft = forms.BooleanField(label="Borrador")
    categories = forms.ChoiceField(label="Categorías")

    class Meta:
        model = Post
        fields = ['title','image_header','post','is_draft','categories']
        labels = ['titlulo','imagen','posteo','borrador','categorçia']
