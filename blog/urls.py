from django.urls import path
from blog.views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
