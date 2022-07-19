from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'blog'

urlpatterns = [
    path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('', cache_page(15 * 60)(HomeView.as_view()), name='home'),
    # path('', HomeView.as_view(), name='home'),
]
