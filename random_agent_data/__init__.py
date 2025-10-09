import random

adjectives = [
    "Shadow", "Fire", "Crimson", "Silver", "Iron", "Storm", "Silent", "Phantom", "Ghost",
    "Golden", "Night", "Steel", "Dark", "Blazing", "Wild", "Frozen", "Scarlet", "Mighty",
    "Rapid", "Hidden", "Fierce", "Thunder", "Eternal", "Vivid", "Cobalt"
]

nouns = [
    "Fox", "Hawk", "Wolf", "Tiger", "Eagle", "Viper", "Falcon", "Dragon", "Panther",
    "Raven", "Lynx", "Cobra", "Bear", "Leopard", "Owl", "Falcon", "Jaguar", "Python",
    "Griffin", "Stingray", "Bison", "Cheetah", "Puma", "Shark", "Falcon"
]

def random_codename():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def random_phone():
    d = [str(random.randrange(10)) for _ in range(10)]
    return '+7' + ''.join(d)