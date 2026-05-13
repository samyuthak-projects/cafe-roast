import tkinter as tk
from customers import CAFE_QUOTES
import random

class CafeRoastUI:
    def __init__(self, cafe):
        self.cafe = cafe

        self.window = tk.Tk()
        self.window.title("☕ Cafe Roast")
        self.window.geometry("800x550")
        self.window.configure(bg="#2b1d17")

        self.banner = tk.Label(self.window, text="☕ CAFE ROAST ☕", font=("Helvetica", 24, "bold"), bg="#2b1d17", fg="#f5e6d3")
        self.banner.pack(pady=20)

        self.label = tk.Label(self.window, text="Welcome to Cafe Roast!", font=("Helvetica", 16, "bold"), bg="#2b1d17", fg="#f5e6d3")
        self.label.pack(pady=20)

        self.info = tk.Label(self.window, text="", font=("Helvetica", 12), bg="#2b1d17", fg="#dbc1ac")
        self.info.pack(pady=10)

        self.button_frame = tk.Frame(self.window, bg="#2b1d17")
        self.button_frame.pack()

        self.quote_label = tk.Label(self.window, text=random.choice(CAFE_QUOTES), bg="#2b1d17", fg="#dbc1ac", font=("Helvetica", 10, "italic"))
        self.quote_label.pack(pady=10)

        self.drink_buttons = []

        row_num = 2

        for drink in self.cafe.drinks:

            button = tk.Button(
                self.button_frame,
                text=f"Brew {drink.title()}",
                command=lambda d=drink: self.brew_drink(d),
                bg="#6f4e37",
                fg="white",
                activebackground="#8b5e3c",
                font=("Helvetica", 10, "bold"),
                width=20
            )

            button.grid(row=row_num, column=1, pady=5)

            self.drink_buttons.append(button)

            row_num += 1

        self.new_customer_button = tk.Button(self.button_frame, text="New Customer", command=self.new_customer, bg="#4a90e2", fg="white", activebackground="#357ab8", font=("Helvetica", 10, "bold"), width=20)
        self.new_customer_button.grid(row=0, column=1, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.window.quit, bg="#dc3545", fg="white", activebackground="#c82333", font=("Helvetica", 10, "bold"), width=20)
        self.quit_button.grid(row=8, column=1, padx=5)

        self.update_ui()

    def update_ui(self):
        stars = "★" * self.cafe.reputation
        self.info.config(text=f"Coins: {self.cafe.coins} | Reputation: {stars} | Weather: {self.cafe.weather}")

    def new_customer(self):
        customer = self.cafe.new_customer()
        self.label.config(text=f"{customer['name']} says: {customer['greeting']} (Wants: {customer['order']})")

    def brew_drink(self, drink):
        result = self.cafe.serve(drink)
        self.label.config(text=result)
        self.update_ui()

    def run(self):
        self.window.mainloop()