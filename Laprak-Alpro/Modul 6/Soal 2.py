"""Buat sebuah himpunan dengan minimal 10 value, yang mana setiap himpunan dapat 
mencakup union, intersection, dan differene"""

nilai1 = {40,50,60,75,85,95}
nilai2 = {40,55,75,80,85,90}

print('Himpunan 1',nilai1)
print('Himpunan 2',nilai2)

gabungan = nilai1.union(nilai2)
print ('Himpunan Gabungan : ',gabungan)

irisan = nilai1.intersection(nilai2)
print ('Himpunan Irisan : ',irisan)

pengurangan = nilai1.difference(nilai2)
print ('Himpunan Pengurangan : ', pengurangan)