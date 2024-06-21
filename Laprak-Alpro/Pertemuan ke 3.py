# x = "wulan" # Contoh 1:
# while x:
#     print(x)
#     x = x[ 1 : 1]

# a = 0; b = 10 # Contoh 2:
# while a < b :
#     print (a)
#     a = a + 1
   
# Bentuk umum perintah for    
# for i in [5, 4, 3, 2, 1]: #Contoh 1
#     print (i)

# T = [(1,2), (3,4), (5,6)]
# for (a,b) in T :
#     print (a,b)

"""nama = ['budi','andi','rudi','sandi']
usia = [20, 18, 22, 19]
for i in range (len(nama)) :
    print (nama[i], 'berusia', usia[i], 'tahun')"""

# x = 4
# while x < 5:
#     if x == 3:
#         break
#     print (x)
#     x = x+1
# else:
#     print ("loop sudah selesai dikerjakan")

# Perintah pass
# Program tidak akan melakukan
# #proses looping 
# while true : pass
# while True : pass

""" Latihan praktikum
Membuat Program For, While dan Break"""
# a=1   # Contoh 1
# while a<5:
#     print (a)
#     a+=2
     
#menampilkam bilangan ganjil
# a=10
# while a<10:
#     a+=1
#     if a%2:
#         print ('%d bilangan ganjil'%a)
#     else:
#         continue

#Menampilkan angka dari 1 sampai 6 dengan menggunakan while
# a=1
# while a<10:
#     print (a)
#     a+=1
#     if a>6:
#         break

# Perintah while menampilkan output tanpa henti
# while  1:
#     print('perulangan tanpa batas tekan, ^C untuk berhenti')

#Menggunakan perintah for untuk menampilkan nama – nama bulan
# bulan={1:'januari',2:'februari',3:'maret',4:'april',5:'mei'}
# for a in bulan.values():
#  print (a)

n = 10
while n:
    n = n + 1
    if n % 2 != 0:
        continue
    print (n)

# i = 1
# while 1 < 7:
#     print (i)
#     if i == 4:
#         break
#     i+=1

# for x in range (0, 20, 3):
#     print (x)

# Prodi = ['SI', 'TIF', 'TI', 'ELEKTRO']
# for x in Prodiif x == "TIF":
#     continue
# print(x)



# #program dengan Outputnya seperti di bawah ini : bintang segitiga sederhana
# a = int(input("masukkan jumlah: ")) # Cara pertama
# for i in range(0, a):
#     for j in range(0, a-1):
#         print(' # ' , end='')
#     a -= 1
#     print('')

# masukkan = int(input('Masukkan Angka : '))
# gambar = ' * '
# kali = masukkan * gambar

# while (kali):
#     print ( kali )
#     if kali == masukkan:
#         break
#     kali = kali[ 1: ] 

