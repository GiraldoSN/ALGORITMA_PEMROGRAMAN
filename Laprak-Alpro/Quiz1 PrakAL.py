while True:
    awal = int(input("masukan angka awal : "))
    akhir = int(input("masukan batas angka : "))
    print("tanda + /")
    tanda = input("Masukan tanda yang diinginkan : ")
    for n in range(1,akhir+1):
        if tanda == "+":
            hasil = awal + n
            print(awal,tanda,n,"=",hasil)
        elif tanda == "/":
            hasil = awal / n
            print(awal,tanda,n,"=",hasil)
        else:
            print("tanda yang anda masukan salah!")
            break
    lanjut = input("ingin lanjut (y/t) ? ")
    if lanjut == "y":
        pass
    elif lanjut == "t":
        print("program berhenti!!!")
        break
    else:
        print("inputan salah")