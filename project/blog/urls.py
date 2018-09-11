from django.urls import path

from django.views.generic import TemplateView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    )

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'),name='blog-about'),


]
