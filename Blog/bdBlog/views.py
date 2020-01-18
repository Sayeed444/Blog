from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView

from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-data_field']

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'home/post_form.html'
    fields = ['title','context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
