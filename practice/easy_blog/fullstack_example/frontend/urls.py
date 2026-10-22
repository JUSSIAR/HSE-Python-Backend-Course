from django.urls import path

from .views import index
from .views import article_list
from .views import article_create

urlpatterns = [
    path('', index),
    path('list/', article_list),
    path('create/', article_create),
]
