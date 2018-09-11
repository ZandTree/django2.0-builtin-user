from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,DetailView,
    CreateView,UpdateView,
    DeleteView
    )
from django.core.paginator import Paginator

#from django.core.urlresolvers  import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/author_post.html'
    context_object_name='posts'
    # т.к. это пее=репишится в методе ниже, то нафиш=г его ordering = ['-date_posted']
    paginate_by = 5
    # перепишем метод: хочу выпилить посты только данного автора
    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    fields = ['title','content']
    model = Post
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    fields = ['title','content']
    model = Post
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'  #reverse_lazy('blog-home')
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

# def auth_post(request,pk):
#     author = User.objects.get(id=pk)
#     #posts = Post.objects.filter(author_id=pk)
#     return render(request,'blog/author_post.html',{'author':author})
# def auth_post(request,pk):
#     posts = Post.objects.filter(author_id=pk)
#     return render(request,'blog/author_post.html',{'posts':posts})
