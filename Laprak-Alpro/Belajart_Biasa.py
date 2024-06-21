#program menghitung harga diskon barang
nama_barang = str(input("masukkan nama barang : "))
harga = int(input("masukkan harga : "))
sepatu = 200000
baju = 150000
celana = 100000


diskon = int(input("masukkan diskon : "))
hasil = harga-harga*diskon/100
print("hasil diskon : ", hasil)


