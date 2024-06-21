"""Membuat program kasir, ketika customer melakukan order
a. Input no meja
b. Input daftar makanan
c. Input harga makanan
d. Total pembayaran dari pelanggan
e. Aplikasi bisa menampilkan dan mengubah data customer yang telah melakukan order"""

dict = {'No Meja': input("No meja : "),'Menu makanan': input('Menu makanan : '), 'Harga': int(input('Harga : '))}
pembayaran = int(input('Masukkan pembayaran : '))
kembalian = pembayaran - dict["Harga"]
baru = str(input('apakah data sudah benar ? '))
if baru == 'tidak':
    dict['No Meja']=input('tempat baru : ')
    dict['Menu makanan']=input('menu baru : ')
    dict['Harga']=input('harga baru')
    print('tempat yang anda pilih',dict['No Meja'],'menu yang anda pilih',dict['Menu makanan'],'harga',dict['Harga'])
    print("Kembalian anda adalah : " , kembalian)
else:
    print('tempat yang anda pilih',dict['No Meja'],'menu yang anda pilih',dict['Menu makanan'],'harga',dict['Harga'])
    print("Kembalian anda adalah : " , kembalian)