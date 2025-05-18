products = []
orders = []


class Customer:
    _id_counter = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = Customer._id_counter
        Customer._id_counter += 1


class Product:
    def __init__(self, product_name, product_brand, amount, price):
        self.product_name = product_name
        self.product_brand = product_brand
        self.amount = amount
        self.price = price

        def show_product(self, product, amount):
            pass


class Order:
    id_counter = 1

    def __init__(self, id_n, customer, date):
        self.id_n = id_n
        self.customer = customer
        self.date = date
        self.total_orders = 0
        self.orders = []

    def add_order(self, product, amount):
        self.orders.append({product.name: amount})
        self.total_orders += product.price * amount

    def showing_order(self):
        print(self.id_n, self.date, self.customer.name, self.total_orders, self.orders)

    # when the admin is adding product to the E-Shop
    def add_product(self, product):
        pass

    def total_price(self):
        pass


# We can also add brand, amount ect
class Admin:
    def __init__(self, username):
        self.username = username

    def add_product(self):
        name = input("Product name: ")
        try:
            price = float(input("Product price: "))
            product = Product(name, price)
            products.append(product)
            print(f"Product {name} added successfully.")
        except ValueError:
            print("Invalid price. Try again")
