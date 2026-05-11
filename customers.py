import random
from drinks import DRINKS

CUSTOMER_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

def create_customer():
    name = random.choice(CUSTOMER_NAMES)
    drink = random.choice(list(DRINKS.keys()))
    
    return {
        "name": name, 
        "order": drink
    }