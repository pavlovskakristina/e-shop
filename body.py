from datetime import date
from storage import save_products_to_file
products = []
orders = []


class Customer:
    _id_counter = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = Customer._id_counter
        Customer._id_counter += 1

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"


class Product:
    def __init__(self, name, brand, amount, price):
        self.name = name
        self.brand = brand
        self.amount = amount
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.brand}) — {self.amount} in stock @ {self.price:.2f}"

    # Funkcja, która wyświetla ekran dla customera.
    def display_for_customer(self, idx=None):
        if idx is not None:
            print(f"{idx}. {self.name} by {self.brand} — {self.price:.2f}$")
        else:
            print(f"{self.name} by {self.brand} — {self.price:.2f}$")


class Order:
    id_counter = 1

    def __init__(self, customer):
        self.id_n = Order.id_counter
        self.customer = customer
        self.date = date.today()
        self.total_orders = 0
        self.orders = []

    def add_order(self, product, amount):
        self.orders.append({product.name: amount})
        self.total_orders += product.price * amount

    def showing_order(self):
        print(self.id_n, self.date, self.customer.name, self.total_orders, self.orders)

    def total_price(self):
        pass


class Admin:
    def __init__(self, username):
        self.username = username

    def add_product(self):
        name = input("Product name: ")
        try:
            price = float(input("Product price: "))
            amount = int(input("Amount of the product: "))
            brand = str(input("Product brand: "))
            product = Product(name, brand, amount, price)
            products.append(product)
            print(f"Product {name} {brand} added successfully. Amount: {amount}")
            #products.append(product)
            save_products_to_file(products)
        except ValueError:
            print("Invalid price. Try again")

    def show_products(self):
        # This functions shows all available products in the e-shop
        print("__________PRODUCTS__________")
        if not products:
            print("No products in inventory")
        else:
            for idx, p in enumerate(products, start=1):
                print(f"{idx}. {p.name} ({p.brand}: {p.amount}) in stock. Price: {p.price:.2f}$")
                print(f"Total price: {(p.price * p.amount)}$")
