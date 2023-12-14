from django.urls import path
from users.views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('view/user/', UserView.as_view(), name='user-view'),
    path('view/user/<int:pk>', UserDetailView.as_view(), name='user-view'),
]
