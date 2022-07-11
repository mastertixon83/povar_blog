from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('', home),
]