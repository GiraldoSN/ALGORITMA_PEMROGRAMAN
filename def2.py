from tracemalloc import start


start
print('Rumus kecepatan\n')
print('+'*100, '\n')

#rumus kecepatan = jarak/waktu
def Kecepatan():
    jarak = float(input("masukkan jarak dalam meter : "))
    waktu = float(input("masukkan waktu dalam detik : "))
    kecepatan = jarak/waktu
    print('kecepatan kelereng menggelinding adalah :', kecepatan, "m/s\n")

#rumus jarak = kecepatan*waktu
def Jarak():
    kecepatan = float(input("masukkan kecepatan dalam m/s : "))
    waktu = float(input("masukkan waktu dalam detik : "))
    jarak = kecepatan*waktu
    print('Jarak tempuh kelereng adalah :', jarak, 'm\n')

#rumus waktu = jarak/kecepatan
def Waktu():
    jarak = float(input("masukkan jarak dalam meter : "))
    kecepatan = float(input("masukkan kecepatan dalam m/s : "))
    waktu = jarak/kecepatan
    print('waktu tempuh kelereng adalah : ', waktu, 's\n')

def menu():
    print('Menu')
    print('1.Kecepatan')
    print('2.Jarak')
    print('3.Waktu')
    print('4.Selesai')

loop = True
while loop:
    menu()
    masukan = input('Masukkan pilihan : ')
    if masukan == '1':
        Kecepatan()
    elif masukan == '2':
        Jarak()
    elif masukan == '3':
        Waktu()
    elif masukan == '4':
        print("Program selesai")
        loop = False    
    else:
        print("Input Invalid")

