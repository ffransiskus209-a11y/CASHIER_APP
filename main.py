"""Simple Cashier — Minggu 01 (Foundation). 
Data produk masih disimpan sebagai dictionary biasa. 
Ini DISENGAJA: keterbatasannya akan terasa di Minggu 02, 
dan itulah alasan kita butuh class. 
""" 
# Satu produk = satu dictionary. 
product = { 
    "code": "P001", 
    "name": "Indomie", 
    "price": 3000, 
    "stock": 20, 
} 
print("Produk pertama:", product["name"]) 
print() 

# Banyak produk = list berisi dictionary. 
products = [ 
    {"code": "P001", "name": "Indomie", "price": 3000, "stock": 20}, 
    {"code": "P002", "name": "Teh Botol", "price": 4000, "stock": 15}, 
    {"code": "P003", "name": "Roti", "price": 7000, "stock": 8}, 
] 

print("=========================") 
print("     SIMPLE CASHIER") 
print("=========================") 
print() 
print() 

for item in products: 
    print(item["code"], item["name"], item["price"], item["stock"]) 

print()

# Menghitung subtotal masih dilakukan manual di setiap tempat. 
quantity = 2 
subtotal = products[0]["price"] * quantity 
print("Subtotal", quantity, products[0]["name"], "=", subtotal) 

print() 
print("--- Catatan untuk Minggu 02 ---") 

# Masalah 1: tidak ada yang mencegah data tidak masuk akal. 
products[0]["price"] = -5000 
products[0]["stock"] = -100 
print("Harga sekarang:", products[0]["price"], "(negatif, tetap diterima)") 
print("Stock sekarang:", products[0]["stock"], "(negatif, tetap diterima)")

# Masalah 2: salah ketik nama key baru ketahuan saat program error. 
# print(products[0]["nama"])   # KeyError: 'nama'
 
# Masalah 3: perilaku (subtotal) terpisah dari datanya.