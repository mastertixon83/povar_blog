from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm


class HomeView(ListView):
    model = Post
    # paginate_by = 10
    template_name = 'blog/home.html'


class PostListView(ListView):
    """Вывод списка постов"""
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    """Вывод одного поста"""
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class AddComment(CreateView):
    """Добавление комментария"""
    model = Comment
    form_class = CommentForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()