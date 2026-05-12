import tkinter as tk

class CafeRoastUI:
    def __init__(self, cafe):
        self.cafe = cafe

        self.window = tk.Tk()
        self.window.title("☕ Cafe Roast")
        self.window.geometry("600x500")

        self.label = tk.Label(self.window, text="Welcome to Cafe Roast!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.info = tk.Label(self.window, text="")
        self.info.pack(pady=10)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.brew_button = tk.Button(self.button_frame, text="Brew Latte", command=self.brew_latte)
        self.brew_button.grid(row=2, column=1, padx=5)

        self.brew_button = tk.Button(self.button_frame, text="Brew Mocha", command=self.brew_mocha)
        self.brew_button.grid(row=3, column=1, padx=5)

        self.brew_button = tk.Button(self.button_frame, text="Brew Cappuccino", command=self.brew_cappuccino)
        self.brew_button.grid(row=4, column=1, padx=5)

        self.brew_button = tk.Button(self.button_frame, text="Brew Espresso", command=self.brew_espresso)
        self.brew_button.grid(row=5, column=1, padx=5)

        self.new_customer_button = tk.Button(self.button_frame, text="New Customer", command=self.new_customer)
        self.new_customer_button.grid(row=0, column=1, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.window.quit)
        self.quit_button.grid(row=6, column=1, padx=5)

        self.update_ui()

    def update_ui(self):
        self.info.config(text=f"Coins: {self.cafe.coins} | Reputation: {self.cafe.reputation}")

    def new_customer(self):
        customer = self.cafe.new_customer()
        self.label.config(text=f"{customer['name']} says: {customer['greeting']} (Wants: {customer['order']})")

    def brew_latte(self):
        result = self.cafe.serve("latte")
        self.label.config(text=result)
        self.update_ui()

    def brew_mocha(self):
        result = self.cafe.serve("mocha")
        self.label.config(text=result)
        self.update_ui()

    def brew_cappuccino(self):
        result = self.cafe.serve("cappuccino")
        self.label.config(text=result)
        self.update_ui()

    def brew_espresso(self):
        result = self.cafe.serve("espresso")
        self.label.config(text=result)
        self.update_ui()

    def run(self):
        self.window.mainloop()