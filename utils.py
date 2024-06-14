import json
from character import Character

def load_characters():
    try:
        with open('data/characters.json', 'r') as file:
            characters_data = json.load(file)
            characters = []
            for data in characters_data:
                name = data.get('name', 'Unnamed')
                age = data.get('age', 0)
                traits = data.get('traits', [])
                experience = data.get('experience', 0)
                events = data.get('events', [])
                character = Character(name, age, traits)
                character.experience = experience
                character.events = events
                characters.append(character)
            return characters
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_characters(characters):
    with open('data/characters.json', 'w') as file:
        json.dump([char.__dict__ for char in characters], file, indent=4)
