print (40*"=")
y = 2
username="Giraldo"
password="12345"
akun = input ("apakah anda sudah memiliki akun XXI?[sudah/belum] : ")
if akun == "belum" :
    print ("silahkan daftarkan akun anda disini : ")
    username = input ("silahkan buat username anda : ")
    password = input ("silahkan buat password anda : ")
    print ("Akun anda telah berhasil dibuat\nsilahkan login")
else :
    print ()
while y == 2:
    user = input("Username : ")
    sandi = input ("password : ")
    if user == username and sandi == password:
        print ("Anda Telah Login")
        y = 0
        while y == 0:
            print ("\n")
            y = 1
            while y == 1:
                daftar = ["1. AVENGERS End Game", "2. Terminator", "3. Toy Story 4", "4. Danur 3", "5. Pariban"]
                print("daftar film yang tesedia : ")
                for i in daftar:
                    print(i)
                film = int(input("pilih film :"))
                if film == 1:
                    print ("Film Avengers End Game")
                    waktu = ["08.00","10.00","13.00","15.00","17.00"]
                    print ("jam tayang yang tersedia ")
                    for i in range (0,len(waktu)):
                        print (i+1,waktu[i])
                    jam = int(input ("silahkan pilih jam tayang : "))
                    harga = 35000
                    jumlahtiket = int(input("jumlah tiket:"))
                    kursi = []
                    for i in range (0,jumlahtiket) :
                        a = input ("silahkan pilih kursi {} :".format(i+1))
                        kursi.append(a)
                    print("totalnya", harga * jumlahtiket)
                    print ("jam tayang yang anda pilih pukul :",waktu[jam-1])
                    print ("anda duduk dikursi :",end=" ")
                    for i in kursi :
                        print (i,end=" ")
                if film == 2:
                    print ("TERMINATOR")
                    waktu = ["08.00", "10.00", "13.00", "15.00", "17.00"]
                    print("jam tayang yang tersedia ")
                    for i in range(0, len(waktu)):
                        print(i + 1, waktu[i])
                    jam = int(input("silahkan pilih jam tayang : "))
                    harga = 35000
                    jumlahtiket = int(input("jumlah tiket:"))
                    kursi = []
                    for i in range (0,jumlahtiket) :
                        a = input ("silahkan pilih kursi {} :".format(i+1))
                        kursi.append(a)
                    print("totalnya", harga * jumlahtiket)
                    print("jam tayang yang anda pilih pukul :", waktu[jam - 1])
                    print("anda duduk dikursi :", end=" ")
                    for i in kursi:
                        print(i, end=" ")
                if film == 3:
                    print ("TOY STORY 4")
                    waktu = ["08.00", "10.00", "13.00", "15.00", "17.00"]
                    print("jam tayang yang tersedia ")
                    for i in range(0, len(waktu)):
                        print(i + 1, waktu[i])
                    jam = int(input("silahkan pilih jam tayang : "))
                    harga = 35000
                    jumlahtiket = int(input("jumlah tiket:"))
                    kursi = []
                    for i in range (0,jumlahtiket) :
                        a = input ("silahkan pilih kursi {} :").format(i+1)
                    print("totalnya", harga * jumlahtiket)
                    print("jam tayang yang anda pilih pukul :", waktu[jam - 1])
                    print("anda duduk dikursi :", end=" ")
                    for i in kursi:
                        print(i, end=" ")
                if film == 4:
                    print ("DANUR 3")
                    waktu = ["08.00", "10.00", "13.00", "15.00", "17.00"]
                    print("jam tayang yang tersedia ")
                    for i in range(0, len(waktu)):
                        print(i + 1, waktu[i])
                    jam = int(input("silahkan pilih jam tayang : "))
                    harga = 35000
                    jumlahtiket = int(input("jumlah tiket:"))
                    kursi = []
                    for i in range (0,jumlahtiket) :
                        a = input ("silahkan pilih kursi {} :").format(i+1)
                    print("totalnya", harga * jumlahtiket)
                    print("jam tayang yang anda pilih pukul :", waktu[jam - 1])
                    print("anda duduk dikursi :", end=" ")
                    for i in kursi:
                        print(i, end=" ")
                if film == 5:
                    print ("PARIBAN")
                    waktu = ["08.00", "10.00", "13.00", "15.00", "17.00"]
                    print("jam tayang yang tersedia ")
                    for i in range(0, len(waktu)):
                        print(i + 1, waktu[i])
                    jam = int(input("silahkan pilih jam tayang : "))
                    harga = 35000
                    jumlahtiket = int(input("jumlah tiket:"))
                    kursi = []
                    for i in range (0,jumlahtiket) :
                        a = input ("silahkan pilih kursi {} :").format(i+1)
                    print("totalnya", harga * jumlahtiket)
                    print("jam tayang yang anda pilih pukul :", waktu[jam - 1])
                    print("anda duduk dikursi :", end=" ")
                    for i in kursi:
                        print(i, end=" ")
                if film == 1 or film == 2 or film == 3 or film == 4 or film == 5:
                    y = 3
                else:
                    print("jenis film yang anda pilih tidak ada, silahkan masukkan  kembali jenis film yang tersedia")
                    y = 1
            print ("\n")
            log = input ("apakah anda ingin keluar? [iya/tidak] : ")
            if log == "tidak":
                y = 0
            else :
                print ("anda sudah keluar")
                break
        y = 2
    else:
        print ("username atau password yang anda masukkan salah, silahkan masukkan kembali")
        y = 2