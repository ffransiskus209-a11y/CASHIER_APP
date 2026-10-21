"""OrderRepository — Minggu 07 (File Handling)."""

import json


class OrderRepository:
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            with open(self.path, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self, orders):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)
