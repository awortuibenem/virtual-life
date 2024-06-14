import random

class Character:
    def __init__(self, name, age, traits):
        self.name = name
        self.age = age
        self.traits = traits
        self.experience = 0
        self.events = []

    def __repr__(self):
        return f"Character(name={self.name}, age={self.age}, traits={self.traits}, experience={self.experience})"

    def add_experience(self, amount):
        self.experience += amount

    def add_event(self, event):
        self.events.append(event)
    
    def interact(self):
        responses = [
    "I'm feeling great today!",
    "It's a tough day, but I'm managing.",
    "I'm excited about the future!",
    "I had a productive day!",
    "Today was challenging, but I learned a lot.",
    "I'm looking forward to the weekend!",
    "I'm enjoying learning new things.",
    "I feel motivated to achieve my goals.",
    "I'm grateful for the support I have.",
    "I'm feeling inspired by recent events.",
    "I'm optimistic about what's ahead.",
    "I'm feeling a bit tired, but I'll push through.",
    "I'm proud of my accomplishments.",
    "I'm reflecting on past experiences.",
    "I'm focused on improving myself.",
    "I'm enjoying the journey of self-discovery.",
    "I'm feeling calm and centered today.",
    "I'm looking forward to spending time with loved ones.",
    "I'm determined to overcome challenges.",
    "I'm feeling creative and innovative.",
]
        print(f"{self.name}: {random.choice(responses)}")
