import modul as mod

print("Selamat datang di program manajemen stok barang!")
print("Pilihan:")
print("1. Tambah data barang")
print("2. Edit data")
print("3. Hapus data barang")
print("4. Cari data")
print("5. Tampilkan data barang")
print("6. Tampilkan jumlah data")
print("7. Keluar")


while True:
    pilih = int(input("Masukkan pilihan: "))
    if pilih == 1:
        print(mod.tambah_data())
    elif pilih == 2:
        print(mod.edit_data())
    elif pilih == 3:
        print(mod.hapus_data())
    elif pilih == 4:
        print(mod.cari_data())
    elif pilih == 5:
        print(mod.tampil_data())
    elif pilih == 6:
        print(mod.tampil_jumlah())
    elif pilih == 7:
        exit()