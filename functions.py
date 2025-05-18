from body import Customer, Product, Order, products, orders
from enum import Enum
import sys

customers = []


def show_menu():
    print(" __________ E-SHOP __________")
    print("""
    1. ADD NEW CUSTOMER 
    2. EXIT 
    3. LOGIN AS ADMIN 
    """)


def customer_interface():
    pass
    # Here we have items to buy


def user_choice():
    show_menu()
    while True:

        try:
            choice = int(input("CHOOSE WHAT YOU WANT TO DO: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            first_name = input("Write your name: ")
            last_name = input("Write your last name: ")
            new_customer = Customer(first_name, last_name)
            print(f"|The customer has been successfully created in the system: "
                  f"{new_customer.first_name} "
                  f"{new_customer.last_name}, "
                  f"ID: {new_customer.id} |")

            customers.append(new_customer)

        # Quiting programme
        elif choice == 2:
            print("PROGRAM FINISHED")
            sys.exit(0)

        # LOGIN as admin to the system
        elif choice == 3:
            if admin_login():
                admin_panel()


def show_all_customers():
    print("ALL CUSTOMERS: ")
    if not customers:
        print("No customers yet")
    for customer in customers:
        print(f"{customer.id}: {customer.first_name} {customer.last_name}")
    print()

def show_product():
    # This functions shows all available products in the e-shop

    print("__________PRODUCTS__________")
    if not products:
        print("No products in inventory")
    else:
        for idx, p in enumerate(products, start=1):
            print(f"{idx}. {p.name} ({p.brand} : {p.amount}) in stock @ {p.price:.2f}")


def admin_login():
    login = input("Username: ")
    password = input("Password: ")

    if login == "admin" and password == "12345":
        print("Logged in successfully.")
        return True
    else:
        print("Incorrect login or password.")
        return False


class AdminPanel(Enum):
    SHOW_CUSTOMERS = 1
    ADD_PRODUCT = 2
    SHOW_PRODUCTS = 3
    SHOW_SALES = 4
    LOGOUT = 5

    def __str__(self):
        return self.name.replace('_', ' ').title()


def admin_panel():
    # Here we ask admin what he wants to do as the admin. We use Enum to
    while True:
        print("\n--- ADMIN PANEL ---")
        for option in AdminPanel:
            print(f"{option.value}. {option}")

        try:
             choice = int(input("Choose option: "))
        except ValueError:
            print("Invalid option. Try again.")
            continue

        if choice == AdminPanel.SHOW_CUSTOMERS.value:
            show_all_customers()

        elif choice == AdminPanel.ADD_PRODUCT.value:
            pass

        elif choice == AdminPanel.SHOW_PRODUCTS.value:
            pass

        elif choice == AdminPanel.SHOW_SALES.value:
            pass

        elif choice == AdminPanel.LOGOUT.value:
            print("Logged out from admin panel." + "\n" * 3)
            show_menu()
            break

