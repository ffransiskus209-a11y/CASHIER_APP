import csv

from models.product import Product

FIELDNAMES = ["code", "name", "price", "stock"]


class ProductRepository:
    def __init__(self, path):
        self.path = path

    def load(self):
        products = []

        try:
            with open(self.path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=",")

                for row in reader:
                    products.append(
                        Product(
                            row["code"],
                            row["name"],
                            int(row["price"]),
                            int(row["stock"]),
                        )
                    )

        except FileNotFoundError:
            return []

        return products

    def save(self, products):
        with open(self.path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES, delimiter=",")
            writer.writeheader()

            for product in products:
                writer.writerow(
                    {
                        "code": product.code,
                        "name": product.name,
                        "price": product.price,
                        "stock": product.stock,
                    }
                )
