
from django.urls import path
from .views import MovieList

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>', MovieList.as_view()),
]