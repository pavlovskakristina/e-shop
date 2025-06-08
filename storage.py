import json
from collections import defaultdict
from body import Customer


def save_products_to_file(products, filename="products.json"):
    with open(filename, "w") as file:
        json.dump([p.__dict__ for p in products], file, indent=4)


def if_products_are_the_same(filename="products.json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

        grouped = defaultdict(lambda: {"name": None,
                                       "brand": None,
                                       "price": 0,
                                       "amount": 0})

        for item in data:
            key = (item["name"],
                   item["brand"],
                   item["price"])

            grp = grouped[key]
            grp["name"] = item["name"]
            grp["brand"] = item["brand"]
            grp["price"] = item["price"]
            grp["amount"] += item.get("amount", 0)

        merged = list(grouped.values())
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(merged, f, indent=4, ensure_ascii=False)

        return merged


def save_customers_to_file(customers, filename="users.json"):
    try:
        with open(filename) as f:
            existing = json.load(f)
    except FileNotFoundError:
        existing = []

    # Dodajemy użytkowników, których jeszcze nie ma
    ids = {c["id"] for c in existing}
    to_save = existing + [
        {"id": c.id,
         "first_name": c.first_name,
         "last_name": c.last_name,
         "password": c.password}
        for c in customers if c.id not in ids
    ]
    # ZAPISUJEMY CAŁOŚć
    with open(filename, "w") as f:
        json.dump(to_save, f, indent=4)


def load_customers_from_file(filename="users.json"):
    loaded = []
    try:
        with open(filename) as f:
            data = json.load(f)
            for item in data:
                c = Customer(item["first_name"], item["last_name"], item["password"])
                c.id = item["id"]
                loaded.append(c)
    except FileNotFoundError:
        pass
    return loaded
