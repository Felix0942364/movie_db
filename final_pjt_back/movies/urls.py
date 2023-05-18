from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('details/<int:pk>', views.details),
    path('watchlists/', views.watchlists),
    path('watchlist/<int:watch_list_pk>/', views.watchlist),
    path('article/<int:article_pk>/mounted/', views.article_mounted)
]