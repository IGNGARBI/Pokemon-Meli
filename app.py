from flask import Flask, jsonify
import requests
import random
from auth import token_required

app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

@app.route('/pokemon/type/<name>', methods=['GET'])
@token_required
def get_pokemon_type(name):
    response = requests.get(f"{POKEAPI_BASE_URL}pokemon/{name}")
    if response.status_code != 200:
        return jsonify({"error": "Pokemon not found"}), 404
    data = response.json()
    types = [t['type']['name'] for t in data['types']]
    return jsonify({"name": name, "types": types})

@app.route('/pokemon/random/<type_name>', methods=['GET'])
@token_required
def get_random_pokemon_by_type(type_name):
    response = requests.get(f"{POKEAPI_BASE_URL}type/{type_name}")
    if response.status_code != 200:
        return jsonify({"error": "Type not found"}), 404
    data = response.json()
    pokemon_list = [p['pokemon']['name'] for p in data['pokemon']]
    random_pokemon = random.choice(pokemon_list)
    return jsonify({"random_pokemon": random_pokemon})

@app.route('/pokemon/longest_name/<type_name>', methods=['GET'])
@token_required
def get_longest_name_pokemon_by_type(type_name):
    response = requests.get(f"{POKEAPI_BASE_URL}type/{type_name}")
    if response.status_code != 200:
        return jsonify({"error": "Type not found"}), 404
    data = response.json()
    pokemon_list = [p['pokemon']['name'] for p in data['pokemon']]
    longest_name_pokemon = max(pokemon_list, key=len)
    return jsonify({"longest_name_pokemon": longest_name_pokemon})

if __name__ == '__main__':
    app.run(debug=True)