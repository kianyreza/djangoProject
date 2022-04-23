from django.urls import path
from ticketing import views

urlpatterns = [
    path('movie/list', views.movie_list),
]
