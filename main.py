from customers import create_customer
from drinks import DRINKS

coins = 20

print("""
☕══════════════════════☕

      CAFE ROAST

☕══════════════════════☕
""")

print("Welcome to Cafe Roast! As the barista, your job is to brew delicious coffee for your customers and earn coins. Each customer will order a drink from the menu, and you can choose to brew it or check the menu. Brew the correct drink to earn coins, but be careful - brewing the wrong drink won't earn you anything! Type 'menu' to see the menu, 'brew' to brew a drink, or 'quit' to end the game. Good luck!")

running = True

while running:

    print("\n-------------")
    print(f"You have {coins} coins.")

    customer = create_customer()

    print(f"{customer['name']} wants a {customer['order']}.")

    print("\nWhat would you like to do?")
    print("\n-menu")
    print("\n-brew")
    print("\n-quit")

    command = input("\n> ").lower()

    if command == "menu":
        print("\n☕ Our menu:")
        for drink, price in DRINKS.items():
            print(f"{drink.title()} - {price} coins")

    elif command == "brew":

        brewed_drink = input("Which drink would you like to brew?\n> ").lower()

        if brewed_drink == customer["order"]:

            reward = DRINKS[brewed_drink]
            coins += reward
            print(f"Perfect! You brewed a {brewed_drink} and earned {reward} coins!")
        
        else:
            print(f"❌ Wrong order! Oh no! You brewed a {brewed_drink} but the customer wanted a {customer['order']}. No coins earned.")

    elif command == "quit":
         
         running = False

print("\nCafe Roast is closed for the day. Thanks for playing!")
    