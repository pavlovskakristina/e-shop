import json


def save_products_to_file(products, filename="products.json"):
    with open(filename, "w") as file:
        json.dump([p.__dict__ for p in products], file, indent=4)
