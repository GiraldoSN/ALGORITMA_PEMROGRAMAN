# Contoh cara membuat dictionary pada python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])

# Update dictionary python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] + 8 # Mengubah entri yang sudah ada 
dict['School'] = "DPS School" # Menambah entri baru

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


Contoh cara menghapus pada Dictionary Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # hapus entry dengan key 'Name'
dict.clear()     # hapus semua entri di dict
del dict         # hapus dictionary yang sudah ada

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict ['School'])

set1 = set() # deklarasi set kosong
set1.add(1) # menambahkan isi set1


A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8}

# # use union function
# A.union(B)
# {1, 2, 3, 4, 5, 6, 7, 8}
# # use union function on B
# B.union(A)
# {1, 2, 3, 4, 5, 6, 7, 8}


# # use intsection functiion on A
# A.intersection(B)
# {4, 5}
# # use intersection function on B
# B.intersection(A)
# {4, 5}


# # use difference function on A
# A.difference(B)
# {1, 2, 3}
# # use - operator on B
# B - A 
# # use difference function B
# B.difference(A)
# {8, 6, 7}


# use symmetric_difference
A.symmetric_difference(B)
{1, 2, 3, 4, 5, 6, 7, 8}
# use symmetric_difference function on B
B.symmetric_difference(A)
{1, 2, 3, 4, 5, 6, 7, 8}
