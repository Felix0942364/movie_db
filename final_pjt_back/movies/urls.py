from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies),
    path('details/<int:pk>', views.get_details),
    path('watchlists/', views.watchlists),
    path('watchlists/<int:watchlist_pk>/', views.watchlist),
    # path('article/<int:article_pk>/mounted/', views.MountedArticle)
]