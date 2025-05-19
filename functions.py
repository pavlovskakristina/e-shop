from body import Customer, Product, Order, Admin, products, orders
from enum import Enum
import sys

customers = []


def show_menu():
    print(" __________ E-SHOP __________")
    print("""
    1. LOG IN  
    2. ADD NEW CUSTOMER  
    3. LOG IN AS ADMIN 
    4. EXIT
    """)


def user_choice():
    show_menu()
    while True:

        try:
            choice = int(input("CHOOSE WHAT YOU WANT TO DO: "))
        except ValueError:
            print("Please enter a valid number.")
            continue


        #  1. Log in as a customer
        #  2. Create profil
        #  3. Log in as an admin
        #  4. Exit

        if choice == 1:
            # Log in as a customer
            pass
        elif choice == 2:
            # Log in as a new customer
            first_name = input("Write your name: ").capitalize().strip()
            last_name = input("Write your last name: ").capitalize().strip()
            new_customer = Customer(first_name, last_name)
            print(f"|The customer has been successfully created in the system: "
                  f"{new_customer.first_name} "
                  f"{new_customer.last_name}, "
                  f"ID: {new_customer.id} |")

            if not products:
                print("No products available yet.")
            else:
                print("AVAILABLE PRODUCTS:")
                for i, product in enumerate(products, start=1):
                    product.display_for_customer(i)

            customers.append(new_customer)

        elif choice == 3:
            # LOGIN as admin to the system
            if admin_login():
                admin_panel()

        elif choice == 4:
            # Quiting programme
            print("PROGRAM FINISHED")
            sys.exit(0)


def show_all_customers():
    print("ALL CUSTOMERS: ")
    if not customers:
        print("No customers yet")
    for customer in customers:
        print(f"{customer.id}: {customer.first_name} {customer.last_name}")
    print()


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
    admin = Admin("admin")        # INSTANCJA KLASY

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
            admin.add_product()

        elif choice == AdminPanel.SHOW_PRODUCTS.value:
            admin.show_products()

        elif choice == AdminPanel.SHOW_SALES.value:
            # Here probably we are going to use some analytics libraries (Pandas, matlplotlib)
            pass

        elif choice == AdminPanel.LOGOUT.value:
            print("Logged out from admin panel." + "\n" * 3)
            show_menu()
            break
