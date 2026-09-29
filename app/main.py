from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

pokemon_data = []

class Pokemon(BaseModel):
    id: int
    name: str
    weight: float
    height: float

class CreatePokemon(BaseModel):
    name: str
    weight: float
    height: float

@app.get("/pokemon/all/{name}")
def read_pokemon(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Data Tidak Ditemukan!"
            )
    data = response.json()
    return data

@app.get("/pokemon/{name}")
def read_pokemon(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="PokeAPI ga bisa dihubungi"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Data Tidak Ditemukan!"
        )

    data = response.json()
    return {
        "id" : data["id"],
        "name" : data["name"],
        "height" : data["height"],
        "weight" : data["weight"],
    }

@app.get("/pokemon/id/{pokemon_id}")
def read_pokemon_by_id(pokemon_id: int):
    for pokemon in pokemon_data:
        if pokemon.id == pokemon_id:
            return pokemon

    raise HTTPException(
        status_code=404,
        detail="Maaf nie, Data tidak ditemukan"
    )

@app.get("/pokemon")
def read_all_pokemon():
    return pokemon_data

@app.post("/pokemon")
def create_pokemon(pokemon: CreatePokemon):
    if not pokemon_data:
        newId = 1
    else: 
        newId = max(pokemon.id for pokemon in pokemon_data) + 1

    newPokemon = Pokemon(
        id = newId,
        name = pokemon.name,
        height = pokemon.height,
        weight = pokemon.weight
    )

    pokemon_data.append(newPokemon)
    return newPokemon

@app.put("/pokemon/id/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: CreatePokemon):
    for idPoke in pokemon_data:
        if idPoke.id == pokemon_id:
            idPoke.name = pokemon.name
            idPoke.weight = pokemon.weight
            idPoke.height = pokemon.height
            return idPoke

    raise HTTPException(
        status_code=404,
        detail="Maaf lagi nie, Data tidak ditemukan!"
    )

@app.delete("/pokemon/id/{pokemon_id}")
def delete_pokemon(pokemon_id:int):
    for idPoke in pokemon_data:
        if idPoke.id == pokemon_id:
            pokemon_data.remove(idPoke)
            return idPoke

    raise HTTPException(
        status_code=404,
        detail="Data tidak ditemukan!"
    )