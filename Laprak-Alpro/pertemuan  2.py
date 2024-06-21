# #Program Perintah if
# nama = "python"
# if nama == "python" :
#     print ("Hallo " + nama)

# Kunci = "Python"
# pasword = input("Masukkan Pasword : ")
# if pasword == Kunci :
#     print("Pasword Benar")
# else:
#     print("Pasword Salah")

# # Program Perintah if-elif-else
# angka = int(input("masukkan sebuah bilangan ="))
# if angka > 0:
#     print("angka positif")
# else:
#     if angka < 0:
#         print("angka biilangan positif")
#     if angka == 0:
#         print("angka yang eliminasi adalah 0")

# nomor_acak = 7
# print ('tebak nomor dari 1-10')
# tebakan = int(input('tebakan anda (bilangan bulat): '))
# if tebakan == nomor_acak:
#     print ('selamat! tebakan anda benar')
#     print ('tapi tidak ada hadiah untuk anda :')
# elif tebakan < nomor_acak:
#     print ('tebakan anda terlalu kecil')
# else:
#     print ('tebakan anda terlalu besar')
#     print ('selesai')

# a=int(input("masukkan umur: "))
# if a <= 15 :
#     print("muda")
# elif a<=20 :

#     print("remaja")
# else:
#     print("tua")

# ploting = int(input("masukkan ploting anda :"))
# if ploting == 1:
#     print("kelas alpro a")
# elif ploting == 2:
#     print ("kelas alprob")
# elif ploting == 3:
#     print ("kelas alpro_b")
# elif ploting == 4:
#     print ("kelas alpro_b")
# else:
#     print("anda bukan mahasiswa alpro")


# nilai = int(input("Nilai :"))
# sisa = nilai % 2
# if sisa == 0:
#     print("GENAP")
# else:
#     print("GANJIL")

# import requests 

# # URL untuk melacak lokasi 
# url = 'https://www.trackmylocation.com/api/location'

# # Mendapatkan data lokasi 
# response = requests.get(url)

# # Mengambil data lokasi 
# location_data = response.json() 

# # Menampilkan nama dan lokasi perangkat yang terhubung ke jaringan 
# for device in location_data['devices']: 
#     print('Nama Perangkat:', device['name'])
#     print('Lokasi:', device['location'])
#     print()

#importing the module 
# import time 
# import pyfiglet 
  
# #using the module 
# ascii_banner = pyfiglet.figlet_format("Unlock Password!") 
# print(ascii_banner) 
  
# #enter the password 
# password = input("Enter the password:") 
  
# #comparing the password 
# if password == "password": 
  
#     #if the password is correct 
#     print("Unlock successful!") 
      
#     #delay for 2 seconds 
#     time.sleep(2) 
  
# else: 
  
#     #if the password is incorrect 
#     print("Incorrect password!") 
      
#     #delay for 2 seconds 
#     time.sleep(2)

# import numpy as np
# import pandas as pd

# # Membuat data sederhana
# data = {'nama': ['Alice', 'Bob', 'Charlie', 'David'],
#         'usia': [25, 32, 45, 28],
#         'pendapatan': [50000, 72000, 95000, 55000]}
# df = pd.DataFrame(data)

# # Menampilkan data
# print(df)

# # Menghitung rata-rata usia
# print("Rata-rata usia: ", df['usia'].mean())

# # Menghitung standar deviasi pendapatan
# print("Standar deviasi pendapatan: ", df['pendapatan'].std())

# import requests

# # URL untuk mengirim pesan
# url = "https://api.whatsapp.com/v1/messages"

# # Data yang dikirimkan dalam permintaan
# data = {
#     "phone_number": "1234567890", # Nomor telepon pelanggan
#     "message": "Hello, how can I help you?", # Pesan yang dikirimkan
#     "auth_token": "your_auth_token" # Token otentikasi untuk akun bisnis WhatsApp Anda
# }

# # Kirim permintaan ke WhatsApp Business API
# response = requests.post(url, json=data)

# # Cek status dari permintaan
# if response.status_code == 200:
#     print("Pesan berhasil dikirim")
# else:
#     print("Terjadi kesalahan: ", response.text)
