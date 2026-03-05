inventory = []

def tambah_barang():
    print("=== Tambah Barang ===")

    kode = input("Kode Barang: ")
    nama = input("Nama Barang: ")
    stok = int(input("Jumlah Stok: "))
    harga = int(input("Harga Barang: "))

    barang = {
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    inventory.append(barang)
    print("Barang berhasil ditambahkan!")


def lihat_barang():
    print()
    print("=== Daftar Persediaan Barang ===")

    if not inventory:
        print("Belum ada barang dalam persediaan.")
        return

    for i, b in enumerate(inventory, start=1):
        print(f"{i}. Kode: {b['kode']} | Nama: {b['nama']} | "
              f"Stok: {b['stok']} | Harga: Rp {b['harga']:,}")


def tambah_stok():
    print("=== Tambah Stok Barang ===")

    kode = input("Masukkan Kode Barang: ")

    for b in inventory:
        if b["kode"] == kode:
            print(f"Barang ditemukan: {b['nama']}")
            tambahan = int(input("Jumlah Stok yang ditambahkan: "))
            b["stok"] += tambahan
            print(f"Stok sekarang: {b['stok']}")
            return

    print("Kode barang tidak ditemukan!")


def kurangi_stok():
    print("=== Kurangi Stok Barang ===")

    kode = input("Masukkan Kode Barang: ")

    for b in inventory:
        if b["kode"] == kode:
            print(f"Barang ditemukan: {b['nama']}")
            kurang = int(input("Jumlah Stok yang dikurangi: "))
            b["stok"] -= kurang
            print(f"Stok sekarang: {b['stok']}")
            return

    print("Kode barang tidak ditemukan!")


def hapus_barang():
    print("=== Hapus Barang ===")

    kode = input("Masukkan Kode Barang yang akan dihapus: ")

    for b in inventory:
        if b["kode"] == kode:
            inventory.remove(b)
            print("Barang berhasil dihapus!")
            return

    print("Kode barang tidak ditemukan!")


def menu():
    while True:
        print("==============================")
        print("  PROGRAM PERSEDIAAN BARANG")
        print("==============================")
        print("1. Tambah Barang")
        print("2. Lihat Semua Barang")
        print("3. Tambah Stok")
        print("4. Kurangi Stok")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_barang()
        elif pilihan == "3":
            tambah_stok()
        elif pilihan == "4":
            kurangi_stok()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid!")

menu()