from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        queryset = Post.objects.all()
        pk = self.kwargs['pk']
        return queryset.get(pk=pk)
