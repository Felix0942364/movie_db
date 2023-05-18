from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.getMovies),
    path('details/<int:pk>', views.getDetails),
    path('watchlists/', views.Watchlists),
    path('watchlist/<int:watch_list_pk>/', views.Watchlist),
    path('article/<int:article_pk>/mounted/', views.MountedArticle)
]