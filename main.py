from functions import user_choice, load_products_from_file, admin_login
from body import products, Admin
import os


def main():
    running_app = 1
    load_products_from_file()

    while running_app:
        if not products:
            print("""There are no products in the inventory. 
Please log in as an administrator and add a product..""")

            while not admin_login():
                os.system('clear')  # Polecenie działa w zależności od systemu operacyjnego.
                print("Invalid data. Try again..")

            # dodawanie towarów
            print("\n Enter the first product")
            admin = Admin("admin")
            admin.add_product()

        user_choice()


if __name__ == "__main__":
    main()
