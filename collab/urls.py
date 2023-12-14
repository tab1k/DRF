from collab.views import IndexView
from django.urls import path, include

app_name = 'collab'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
