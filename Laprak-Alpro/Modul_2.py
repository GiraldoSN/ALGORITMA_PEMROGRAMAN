#program python untuk menentukan sebuah bilangan termasuk bilangan positif atau negatif
angka = int(input("masukkan bilangan :"))
if angka >= 0:
    print("bilangan postif")
else:
    if angka < 0:
        print("bilangan negatif")

a = int(input("masukkan bilangan pertama:"))
b = int(input("masukkkan bilangan kedua :"))
if a > b:
    print (b)
    print(a)
elif a < b:
    print (b)
    print (a)
else :
    print (a)
    print(b)
        
#sebuah program berupa permainan (gunting/batu/kertas) yang dapat dimainkan oleh dua orang. Kedua pemain menginput pilihan masing-masing (batu/gunting/kertas), kemudian komputer melakukan perbandingan untuk melihat siapa yang menangan siapa yang kalah

print('')
print('===========================') 
print('')

print ('0 = Batu , 1 = Gunting , 2 = Kertas dan Masukkan Pilihanmu')
pemain1 = int(input('Masukkan Pilihanmu Pemain 1 : '))
pemain2 = int(input('Masukkan Pilihanmu Pemain 2 : '))

# Batu
if pemain1 == 0 and pemain2 == 0:
    print('Permainan Seri')
elif pemain1 == 0 and pemain2 == 1:
    print('Pemain 1 Menang')
    print ('Pemain 2 Kalah')
elif pemain1 == 0 and pemain2 == 2:
    print('Pemain 1 Kalah ')
    print('Pemain 2 Menang')
# Gunting
elif pemain1 == 1 and pemain2 == 1 :
    print('Hasil Seri')
elif pemain1 == 1 and pemain2 == 0 :
    print ('Pemain 1 Kalah') 
    print ('Pemain 2 Menang ')
elif pemain1 == 1 and pemain2 == 2:
    print ('Pemain 1 Menang')
    print ('Pemain 2 Kalah')
# Kertas
elif pemain1 == 2 and pemain2 == 2 :
    print ('Hasil Seri')
elif pemain1 == 2 and pemain2 == 0 :
    print ('Pemain 1 Menang')
    print ('Pemain 2 Kalah')
elif pemain1 == 2 and pemain2 == 1 :
    print ('Pemain 1 Kalah')
    print ('Pemain 2 Menang')

else :
    print ('Angka Yang Anda Masukkan Salah')

print ('')
print ('=== TERIMA KASIH ===')