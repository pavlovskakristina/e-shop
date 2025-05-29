import json
from collections import defaultdict


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
