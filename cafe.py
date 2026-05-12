import random
from customers import create_customer
from drinks import DRINKS

class Cafe:
    def __init__(self):
        
        self.coins = 20
        self.reputation = 1
        self.current_customer = None

    def new_customer(self):
        self.current_customer = create_customer()
        return self.current_customer
    
    def serve(self, drink):
        if self.current_customer is None:
            return "No customer to serve!"
        
        if drink == self.current_customer["order"]:
            reward = DRINKS[drink]
            self.coins += reward
            self.reputation += 1

            tip = random.randint(0, 3)
            self.coins += tip

            return f"Perfect! +{reward} coins and + {tip} tip!"
        
        else:
            self.reputation -= 1
            return f"❌ Wrong order! The customer wanted a {self.current_customer['order']}. No coins earned."
        

