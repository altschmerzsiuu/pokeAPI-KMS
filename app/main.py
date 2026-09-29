from fastapi import FastAPI
from fastapi import HTTPException
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

@app.get("/pokemon/{name}")
def read(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Data Tidak Ditemukan!"
        )

    data = response.json()
    return data

@app.get("/pokemon/id/{id}")
def read_onedata(id: int):
    for pokemon in pokemon_data:
        if pokemon.id == id:
            return pokemon

    raise HTTPException(
        status_code=404,
        detail="Maaf nie, Data tidak ditemukan"
    )

@app.get("/pokemon")
def read_all():
    return pokemon_data

@app.post("/pokemon")
def create(pokemon: CreatePokemon):
    if not pokemon_data:
        newId = 1
    else: 
        newId = max(pokemon.id for pokemon in pokemon_data) + 1

    pokemonBaru = Pokemon(
        id = newId,
        name = pokemon.name,
        height = pokemon.height,
        weight = pokemon.weight
    )

    pokemon_data.append(pokemonBaru)
    return pokemonBaru

@app.put("/pokemon/id/{id}")
def updatePokemon(id: int, pokemon: CreatePokemon):
    for idPoke in pokemon_data:
        if idPoke.id == id:
            idPoke.name = pokemon.name
            idPoke.weight = pokemon.weight
            idPoke.height = pokemon.height
            return idPoke

    raise HTTPException(
        status_code=404,
        detail="Maaf lagi nie, Data tidak ditemukan!"
    )

@app.delete("/pokemon/id/{id}")
def deletePokemon(id:int):
    for idPoke in pokemon_data:
        if idPoke.id == id:
            pokemon_data.remove(idPoke)
            return idPoke

    raise HTTPException(
        status_code=404,
        detail="Data tidak ditemukan!"
    )