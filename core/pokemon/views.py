from django.shortcuts import render
import requests
import os

BASE_URL = "https://pokeapi.co/api/v2/"


# Create your views here.
def pokemon_index(request):
    url = f"{BASE_URL}pokemon/"
    response = requests.get(url)
    data = response.json()

    all_pokemon = []

    for pokemon in data["results"]:
        url = pokemon["url"]
        response = requests.get(url)
        data = response.json()
        print(data)

        all_pokemon.append(data)

    return render(request, "pokemon.html", {"all_pokemon": all_pokemon})
