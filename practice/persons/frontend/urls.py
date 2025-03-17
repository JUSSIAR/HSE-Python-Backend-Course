from django.urls import path

from frontend import views

urlpatterns = [
    path('', views.index),
    path('list/', views.persons_list),
    path('create/', views.person_create),
]
