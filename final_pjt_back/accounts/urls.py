from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_pk>/', views.profile),
    path('profile/<int:user_pk>/follow/', views.follow),
    path('profile/<int:user_pk>/followers/', views.follower),
    path('profile/<int:user_pk>/followings/', views.following),
]