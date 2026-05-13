import random
from customers import create_customer
from drinks import DRINKS
import json

class Cafe:
    def __init__(self):
        
        self.coins = 20
        self.drinks = list(DRINKS.keys())
        self.reputation = 1
        self.current_customer = None
        self.load_game()

    def new_customer(self):
        self.current_customer = create_customer()
        return self.current_customer
    
    def serve(self, drink):
        if self.current_customer is None:
            return "No customer to serve!"
        
        if drink == self.current_customer["order"]:
            reward = DRINKS[drink]
            self.coins += reward
            self.reputation = min(5, self.reputation + 1)

            tip = random.randint(0, 3)
            self.coins += tip

            self.current_customer = None

            self.save_game()

            return f"Perfect! +{reward} coins and + {tip} tip!"
        
        else:
            self.reputation = max(0, self.reputation - 1)
            prev_order = self.current_customer["order"]
            self.current_customer = None
            return f"Wrong order! The customer wanted a {prev_order}. No coins earned."
        
    def save_game(self):
        data = {"coins": self.coins, "reputation": self.reputation}

        with open("save.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_game(self):
        try:
            with open("save.json", "r") as file:
                data = json.load(file)
                self.coins = data["coins"]
                self.reputation = data["reputation"]
        except:
            pass
    