from django.contrib import admin
from django.urls import path
#from app reviews
from .views import ReviewView
#from .views import index_movies, MovieView


urlpatterns = [
    path('', ReviewView.as_view(), name='review'),
   
]