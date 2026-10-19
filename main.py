from models.product import DigitalProduct, FoodProduct, Product
from models.product_catalog import ProductCatalog
from services.action_history import ActionHistory
from services.order_queue import OrderQueue

catalog = ProductCatalog()

catalog.add(Product("P001", "Indomie", 3000, 20))
catalog.add(Product("P002", "Teh Botol", 4000, 15))
catalog.add(Product("P003", "Teh Kotak", 3500, 10))
catalog.add(FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"))
catalog.add(DigitalProduct("D001", "E-Book Python", 50000, 99))

print("==================")
print("  SIMPLE CASHIER  ")
print("==================")
print()

print("--- Daftar produk ---")
for item in catalog.all():
    # all() mengembalikan list: yang dibutuhkan di sini adalah urutan.
    print(item.code, "", item.get_description())

print()
print("--- Ambil produk lewat code ---")
found = catalog.get("F001")
print("catalog.get('F001') ->", found.get_description())

missing = catalog.get("P999")
print("catalog.get('P999') ->", missing, "(tidak error, hanya None)")

print()
print("--- Cari produk lewat nama ---")
for keyword in ["teh", "TEH", "mie", "kopi"]:
    hasil = catalog.search(keyword)
    nama = [item.name for item in hasil] if hasil else "tidak ditemukan"
    print(f"search({keyword!r}) -> {nama}")

print()
print("--- Hapus produk ---")
catalog.remove("P002")
print("Setelah remove('P002'):", [item.code for item in catalog.all()])

catalog.remove("P002")
print("remove('P002') sekali lagi tidak menjatuhkan program.")

print()
print("--- Antrean order (FIFO) ---")
# Order sungguhan baru dibuat di Minggu 10.
# Untuk sekarang cukup teks sederhana sebagai penanda antrean.
queue = OrderQueue()
queue.enqueue("ORD-001 Indomie x2")
queue.enqueue("ORD-002 Teh Botol x1")
queue.enqueue("ORD-003 Roti x3")

print("Masuk : ORD-001, ORD-002, ORD-003")
print("Keluar:", queue.dequeue())
print("Keluar:", queue.dequeue())
print("Keluar:", queue.dequeue())
print("Antrean kosong ->", queue.dequeue(), "(tidak error)")
print("Yang pertama masuk, pertama juga dilayani.")

print()
print("--- Riwayat tindakan (LIFO) ---")
history = ActionHistory()
history.push("tambah Indomie x2")
history.push("tambah Teh Botol x1")
history.push("tambah Roti x3")

print("Dilakukan:", "tambah Indomie x2, tambah Teh Botol x1, tambah Roti x3")
print("Undo     :", history.pop())
print("Undo     :", history.pop())
print("Undo     :", history.pop())
print("Riwayat kosong ->", history.pop(), "(tidak error)")
print("Yang terakhir dilakukan, pertama dibatalkan.")

print()
print("--- Queue vs Stack ---")
print("Queue (antrean order) : FIFO -> masuk A B C, keluar A B C")
print("Stack (undo)          : LIFO -> masuk A B C, keluar C B A")

print()
print("--- Mengapa dictionary untuk katalog? ---")
print("Katalog dicari berdasarkan code -> dictionary, satu langkah.")
print("Daftar tampilan mementingkan urutan -> list.")
print("Hasil pencarian bisa nol/satu/banyak -> list.")
print("Antrean order dilayani berurutan -> queue (deque).")
print("Undo membatalkan yang terakhir -> stack (list).")
