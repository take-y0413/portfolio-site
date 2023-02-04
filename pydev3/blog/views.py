from django.views.generic.base import TemplateView
from django.views import generic
from .forms import BlogCreateForm
from .models import Post

class Hello(TemplateView):
    template_name = 'blog/hello.html'

class BlogCreate(generic.CreateView):
     form_class = BlogCreateForm
     template_name = 'blog/blog_create.html'
     success_url = '/blog/hello'

class BlogList(generic.ListView):
    model = Post
    template_name = 'blog/blog_list.html'