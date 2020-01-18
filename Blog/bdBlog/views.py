from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-data_field']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'home/post_form.html'
    fields = ['title','context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserPostListView(ListView):
    model = Post
    template_name = 'home/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-data_field')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','context']
    template_name = 'home/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'home/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
