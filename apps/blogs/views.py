from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView

# Models
from apps.blogs.models import Post
from apps.categories.models import Category

from apps.comments.models import Comment

# Forms
from apps.comments.forms import CreateCommentForm
from apps.core.mixins import WriterRequiredMixins


class PostsFeedView(ListView):
    """list view"""
    
    template_name = 'pages/post/index.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posteos'
    queryset = Post.objects.filter(is_draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    
class PostDetailView(DetailView):
    """Detail post."""
    template_name = 'pages/post/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'


    def get_queryset(self):
        return Post.objects.filter(is_draft=False)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=self.get_object()).all()
        context['form_comments'] = CreateCommentForm()
        return context

class CreatePost(WriterRequiredMixins,CreateView):
    model = Post
    template_name = 'pages/post/create-blog.html'
    fields = ('__all__')
    success_url = '/'


def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            # 'profile': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('blogs:detail', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)

def redirect_blogs(request):
    if request.path == 'blogs/post/':
        return redirect('blogs:blogs')
