stok = []

def tambah_data():
    input_nama = str(input("masukan nama barang : "))
    input_stok = int(input("masukan stok barang : "))
    stok_sementara = {"nama_barang" : input_nama , "stok_barang" : input_stok}
    stok.append(stok_sementara)
    return "--- Data berhasil ditambahkan ---"

def edit_data():
    index = int(input("Hapus data index ke : "))
    nama = input("Masukkan nama barang : ")
    jumlah = int(input("Masukkan stok barang : "))
    stok_baru = {"nama_barang" : nama , "stok_barang" : jumlah}
    stok[index] = stok_baru
    return "--- Data telah diubah ---"

def hapus_data():
    index = int(input("hapus data index ke : "))
    stok.pop(index)
    return "--- Data berhasil dihapus ---"    

def cari_data():
    cari = str(input("Cari nama barang : "))
    items = []
    for i in stok:
        if cari in i["nama_barang"]:
            items.append(i)
    if items:
        for item in items:
            return f"{item['nama_barang']} : {item['stok_barang']}"
    else:
        return "Data barang kosong"
    
def tampil_data():
    for i in stok:
        print(f"{i['nama_barang']} : {i['stok_barang']}")
    return ""

def tampil_jumlah():
    jumlah = f"Jumlah  data terimpan {len(stok)}"
    return jumlah