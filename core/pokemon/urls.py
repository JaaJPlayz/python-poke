from django.urls import path
from . import views

urlpatterns = [
    path("pokemon", views.pokemon_index),
]
