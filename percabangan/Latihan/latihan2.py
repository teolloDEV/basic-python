# Mencari nilai tengah dari 3 angka

a, b, c = (
    int(input('Masukkan nilai A : ')),
    int(input('Masukkan nilai B : ')),
    int(input('Masukkan nilai C : '))
)
if (b > a > c) or (c > a > b) :
    print('A menjadi nilai tengah')
elif ( a > b > c) or (c > b > a):
    print('B menjadi nilai tengah')
else:
    print('C menjadi nilai tengah')