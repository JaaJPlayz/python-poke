from django.shortcuts import render
import requests

BASE_URL = "https://pokeapi.co/api/v2/"


# Create your views here.
def pokemon_index(request):
    url = f"{BASE_URL}pokemon?limit=100&offset=0"
    response = requests.get(url)
    data = response.json()

    all_pokemon = []

    for pokemon in data["results"]:
        url = pokemon["url"]
        response = requests.get(url)
        data = response.json()

        all_pokemon.append(data)

    return render(request, "pokemon.html", {"all_pokemon": all_pokemon})
