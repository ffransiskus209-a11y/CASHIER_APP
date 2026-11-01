# UTS Checkpoint (Minggu 08)

## 1. Cakupan Requirement per Minggu
- **Minggu 02-03 (Class, Object, Encapsulation):** `Product` memiliki properti read-only `price`, method `subtotal()`, `change_price()`, dan `reduce_stock()` yang memvalidasi input.
- **Minggu 04 (Inheritance & Polymorphism):** `FoodProduct` dan `DigitalProduct` mewarisi `Product` dan meng-override `get_description()`.
- **Minggu 05 (List & Dictionary):** `ProductCatalog` menggunakan dictionary untuk `get()` O(1) dan list untuk iterasi `search()`.
- **Minggu 06 (Stack & Queue):** `OrderQueue` (FIFO) dan `ActionHistory` (LIFO) berjalan sesuai fungsinya.
- **Minggu 07 (File Handling):** `ProductRepository` membaca CSV, `OrderRepository` membaca JSON. Menangani `FileNotFoundError` dengan mengembalikan list kosong.

## 2. Temuan dan Tindakan
- **Temuan:** `main.py` sebelumnya hanya mendemonstrasikan materi minggu terakhir.
- **Tindakan:** Menulis ulang `main.py` agar mendemonstrasikan alur utuh dari Minggu 02 hingga 07 secara berurutan. Tidak ada fitur baru yang ditambahkan.
- **Temuan:** File database di masa depan berisiko ter-commit.
- **Tindakan:** Menambahkan `*.db` dan `*.sqlite3` ke `.gitignore`.

## 3. Hasil Pemeriksaan Batas Lapisan
- Perintah `findstr` untuk mencari `open(`, `import csv`, dan `import json` di luar `repositories/` **tidak menemukan apa pun**. 
- Seluruh akses berkas sudah terisolasi di dalam folder `repositories/`. Aman untuk penggantian ke Database di Minggu 09.

## 4. Skenario Demo
1. **Encapsulation:** Menunjukkan `subtotal(2)` menghasilkan 6000, dan `price` tidak bisa diubah sembarangan.
2. **Polymorphism:** Satu loop `for` mencetak tiga format produk berbeda tanpa mengecek tipe data.
3. **Repository:** Memuat 4 produk dari CSV, dan mengembalikan list kosong saat file tidak ada.
4. **Dictionary:** Mencari "P001" langsung mendapat hasil, dan mencari "P999" mengembalikan `None` tanpa error.
5. **Search:** Pencarian "teh" dan "TEH" keduanya mengembalikan produk yang sama (case-insensitive).
6. **Queue (FIFO):** Memasukkan A, B, C dan keluar berurutan A, B, C.
7. **Stack (LIFO):** Memasukkan A, B, C dan keluar terbalik C, B, A.
8. **Alur Penuh:** Menjual 3 Indomie, memotong stock, dan menyimpannya ke file.
9. **Persistensi:** Membaca ulang file CSV membuktikan stock berkurang dan tersimpan permanen.
10. **Order tersimpan:** File JSON mencatat transaksi yang baru saja terjadi.

## 5. Rantai yang Harus Dapat Dijelaskan
`Class -> Object -> Data Structure -> Repository -> File`
- **Class:** Blueprint (`Product`).
- **Object:** Instance nyata (`Product("P001", ...)`).
- **Data Structure:** Wadah objek (`ProductCatalog` dengan list & dict).
- **Repository:** Pengatur lalu lintas file (`ProductRepository`).
- **File:** Media fisik (`data/products.csv`).

## 6. Keadaan yang Dibawa ke Minggu 09
- Struktur lapisan sudah bersih.
- `.gitignore` siap menampung file database.
- Ujung rantai (`File`) siap diganti menjadi `Database` (SQLite/MySQL) tanpa mengubah `models/` atau `services/`.