import random
from drinks import DRINKS

CUSTOMER_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

GREETINGS = ["Long day today... ", "I could really use a pick-me-up! ", "I need my caffeine fix! ", "Can you make me something delicious? ", "I'm in the mood for something special! "]

def create_customer():
    name = random.choice(CUSTOMER_NAMES)
    drink = random.choice(list(DRINKS.keys()))
    greeting = random.choice(GREETINGS)
    
    return {
        "name": name, 
        "order": drink,
        "greeting": greeting
    }