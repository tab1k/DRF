from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(TokenObtainPairView):
    pass


class UserView(generics.ListCreateAPIView):
    users = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.users


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])

