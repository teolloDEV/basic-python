# menggunakn pop()
# menghapus dan mengambil angka terkhir
# data bisa disimpan di pop()

print('menghapus dengan fungsi pop() ')
list_angka = [1, 2, 3, 4, 5]
print(list_angka)
hapus = list_angka.pop()
print('angka yang terhapus', hapus)
print(list_angka)

print('\nMenghapus dengan fungsi remove')

# menghapus sama dengan nilai yang dimasukkan

list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)
list_buah.remove('Jeruk')
print(list_buah)

print('\nMenghapus dengan fungsi del')
list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)
del list_buah[:1]
print(list_buah)