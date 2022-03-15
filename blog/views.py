from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse
from django.shortcuts  import get_object_or_404 
from .models import Post
from time import timezone

class BlogView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_object(self, **kwargs):
        return get_object_or_404(Post, slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] =  self.get_object()
        return context