import random

def random_event(character):
    events = [
        {"description": "won a scholarship", "experience": 10},
        {"description": "faced a health issue", "experience": -5},
        {"description": "got a job offer", "experience": 15},
        {"description": "adopted a pet", "experience": 5},
        {"description": "traveled to a new country", "experience": 20},
        {"description": "started a new hobby", "experience": 8},
        {"description": "learned a new skill", "experience": 12},
        {"description": "celebrated a birthday", "experience": 5},
        {"description": "completed a challenging project", "experience": 18},
        {"description": "helped a friend in need", "experience": 7},
        {"description": "experienced a natural disaster", "experience": -15},
        {"description": "won a sports competition", "experience": 12},
        {"description": "met a famous person", "experience": 10},
        {"description": "volunteered for a charity", "experience": 9},
        {"description": "published an article or book", "experience": 15},
    ]
    event = random.choice(events)
    character.add_event(event)
    character.add_experience(event["experience"])
    return event
