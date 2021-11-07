# Author: Nhat Nguyen
# The following program takes a list of Pokemon and pulls from the PokeAPI information about
# each Pokemon and storing it into their individual json file

# ---------------------------------------------------------------------------------------------------
# PokeAPI function
# ---------------------------------------------------------------------------------------------------
import requests
import json

def PokeAPI(pokemonName):
    
	pokemonAPI = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemonName)
	pokemonData = pokemonAPI.text
	pokemonJson = json.loads(pokemonData)
	
	pokeName = pokemonJson['name']#as a string
	pokeType = pokemonJson['types'][0]['type']['name']#as a string
	
	move0URL = pokemonJson['moves'][0]['move']['url']
	move0API = requests.get(move0URL)
	move0Data = move0API.text
	move0Json = json.loads(move0Data)
	move0Name = move0Json['name']#as a string
	move0Power = move0Json['power']#as an int
	move0PP = move0Json['pp']#as an int
	move0Type = move0Json['type']['name']#as a string
	
	move1URL = pokemonJson['moves'][1]['move']['url']
	move1API = requests.get(move1URL)
	move1Data = move1API.text
	move1Json = json.loads(move1Data)
	move1Name = move1Json['name']#as a string
	move1Power = move1Json['power']#as an int
	move1PP = move1Json['pp']#as an int
	move1Type = move1Json['type']['name']#as a string
	
	move2URL = pokemonJson['moves'][2]['move']['url']
	move2API = requests.get(move2URL)
	move2Data = move2API.text
	move2Json = json.loads(move2Data)
	move2Name = move2Json['name']#as a string
	move2Power = move2Json['power']#as an int
	move2PP = move2Json['pp']#as an int
	move2Type = move2Json['type']['name']#as a string
	
	move3URL = pokemonJson['moves'][3]['move']['url']
	move3API = requests.get(move3URL)
	move3Data = move3API.text
	move3Json = json.loads(move3Data)
	move3Name = move3Json['name']#as a string
	move3Power = move3Json['power']#as an int
	move3PP = move3Json['pp']#as an int
	move3Type = move3Json['type']['name']#as a string
	
	stat0Name = pokemonJson['stats'][0]['stat']['name']#as a string
	stat0Base = pokemonJson['stats'][0]['base_stat']#as an int
	
	stat1Name = pokemonJson['stats'][1]['stat']['name']#as a string
	stat1Base = pokemonJson['stats'][1]['base_stat']#as an int
	
	stat2Name = pokemonJson['stats'][2]['stat']['name']#as a string
	stat2Base = pokemonJson['stats'][2]['base_stat']#as an int
	
	stat3Name = pokemonJson['stats'][3]['stat']['name']#as a string
	stat3Base = pokemonJson['stats'][3]['base_stat']#as an int

	stat4Name = pokemonJson['stats'][4]['stat']['name']#as a string
	stat4Base = pokemonJson['stats'][4]['base_stat']#as an int
	
	stat5Name = pokemonJson['stats'][5]['stat']['name']#as a string
	stat5Base = pokemonJson['stats'][5]['base_stat']#as an int

	
	f = open("Pokemon_json/" + pokemonName + ".json", "w")
	
	f.write('{\n    "name": "')
	f.write(pokeName)
	f.write('",\n    "type": "')
	f.write(pokeType)
	f.write('",\n    "moves": [\n        ')
	
	f.write('{\n            "name": "')
	f.write(move0Name)
	f.write('",\n            "power": ')
	f.write(str(move0Power))
	f.write(',\n            "pp": ')
	f.write(str(move0PP))
	f.write(',\n            "type": "')
	f.write(move0Type)
	f.write('"\n        },\n        ')
	
	f.write('{\n            "name": "')
	f.write(move1Name)
	f.write('",\n            "power": ')
	f.write(str(move1Power))
	f.write(',\n            "pp": ')
	f.write(str(move1PP))
	f.write(',\n            "type": "')
	f.write(move1Type)
	f.write('"\n        },\n        ')
	
	f.write('{\n            "name": "')
	f.write(move2Name)
	f.write('",\n            "power": ')
	f.write(str(move2Power))
	f.write(',\n            "pp": ')
	f.write(str(move2PP))
	f.write(',\n            "type": "')
	f.write(move2Type)
	f.write('"\n        },\n        ')
	
	f.write('{\n            "name": "')
	f.write(move3Name)
	f.write('",\n            "power": ')
	f.write(str(move3Power))
	f.write(',\n            "pp": ')
	f.write(str(move3PP))
	f.write(',\n            "type": "')
	f.write(move3Type)
	f.write('"\n        }\n        ')
	
	f.write('    ],\n')
	f.write('    "stats": [\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat0Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat0Base))
	f.write('\n        },\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat1Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat1Base))
	f.write('\n        },\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat2Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat2Base))
	f.write('\n        },\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat3Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat3Base))
	f.write('\n        },\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat4Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat4Base))
	f.write('\n        },\n')
	
	f.write('        {\n')
	f.write('            "name": "')
	f.write(stat5Name)
	f.write('",\n            "base_stat": "')
	f.write(str(stat5Base))
	f.write('\n        }\n    ]\n}')

pokemonFile = open("pokemon_list.txt")

pokemonList =  pokemonFile.read().splitlines()


for x in pokemonList:
    try:
        PokeAPI(x.lower())
    except:
       print("pokemon " + x + " does not exist") 

