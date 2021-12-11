
from django.shortcuts import render
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

class BlogHomePageView(TemplateView):
     template_name='blog/index.html'

     def get_context_date(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['posts']= Post.postobjects.all()
         return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_date(self, **kwargs):
         context = super().get_context_data(**kwargs)
         post = Post.objects.filter(slug=self.kwargs.get('slug'))
         return context