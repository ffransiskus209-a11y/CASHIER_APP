"""Simple Cashier — Minggu 07 (File Handling & Persistence)."""

from models.product_catalog import ProductCatalog
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.action_history import ActionHistory
from services.order_queue import OrderQueue

PRODUCTS_PATH = "data/products.csv"
ORDERS_PATH = "data/orders.json"

product_repository = ProductRepository(PRODUCTS_PATH)
order_repository = OrderRepository(ORDERS_PATH)

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

print("--- Muat produk dari CSV ---")

catalog = ProductCatalog()

for product in product_repository.load():
    catalog.add(product)

for item in catalog.all():
    print(item.code, "|", item.name, "| harga", item.price, "| stock", item.stock)

print()
print("--- File tidak ada ---")

kosong = ProductRepository("data/tidak_ada.csv")
print("load() ->", kosong.load(), "(FileNotFoundError ditangani)")

print()
print("--- Transaksi lalu simpan ---")

indomie = catalog.get("P001")
history = ActionHistory()
queue = OrderQueue()

orders = order_repository.load()
jumlah = 3

print("Stock Indomie sebelum:", indomie.stock)

if indomie.stock >= jumlah:
    indomie.reduce_stock(jumlah)

    nomor_order = len(orders) + 1
    order = f"ORD-{nomor_order:03d} Indomie x{jumlah}"

    queue.enqueue(order)
    orders.append(queue.dequeue())
    history.push(f"Penjualan Indomie x{jumlah}")

    product_repository.save(catalog.all())
    order_repository.save(orders)

    print("Stock Indomie sesudah:", indomie.stock)
    print("Perubahan ditulis ke data/products.csv dan data/orders.json")
else:
    print("Stock Indomie tidak cukup.")
    print("Isi ulang stock di", PRODUCTS_PATH, "untuk mencoba lagi.")

print()
print("--- Baca ulang dari file ---")

segar = ProductRepository(PRODUCTS_PATH).load()
indomie_lagi = next(p for p in segar if p.code == "P001")

print("Stock Indomie setelah dibaca ulang:", indomie_lagi.stock)
print("Order tersimpan:", OrderRepository(ORDERS_PATH).load())

print()
print("--- Mengapa CSV dan JSON? ---")
print("Produk berbentuk tabel datar         -> CSV.")
print("Order berisi daftar item di dalamnya -> JSON.")
