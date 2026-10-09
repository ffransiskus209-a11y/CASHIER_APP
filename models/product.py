"""Model Product Minggu 04 (Inheritance & Polymorphism).

Menggabungkan Product dasar dengan class turunan FoodProduct dan DigitalProduct.
"""


class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        # Garis bawah penanda: ini state internal, jangan disentuh dari luar.
        self._price = price
        self._stock = stock

    @property
    def price(self):
        # Boleh dibaca, tidak boleh ditulis langsung.
        return self._price

    @property
    def stock(self):
        return self._stock

    def subtotal(self, quantity):
        return self._price * quantity

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            raise ValueError("Insufficient stock")
        self._stock -= quantity

    def get_description(self):
        # Perilaku dasar. Subclass boleh menggantinya (override).
        return self.name


class FoodProduct(Product):
    def __init__(self, code, name, price, stock, expiry_date):
        super().__init__(code, name, price, stock)
        self.expiry_date = expiry_date

    def get_description(self):
        return f"{self.name} Expired: {self.expiry_date}"


class DigitalProduct(Product):
    def __init__(self, code, name, price, stock):
        super().__init__(code, name, price, stock)

    def get_description(self):
        return f"{self.name} Digital Product"