#  input secara statis

a = 3
b = 2
c = a + b
print(a, '+', b, '= ', c)

# input oleh user

print('program mencari luas persegi panjang')

panjang = input('Masukkan panjang persegi : ')
lebar = input('Masukkan lebar persegi : ')

# karena yang di input bukan string maka tambahkan type datanya
# int(panjang), int(lebar)
print('Luas persegi panjang adalah : ', int(panjang) * int(lebar))
