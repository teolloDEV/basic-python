# mencari angka terbesar dari tiga angka

# cara 1
# a = int(input('Masukkan angka pertama : '))
# b = int(input('Masukkan angka kedua : '))
# c = int(input('Masukkan angka ketiga : '))

# Cara 2

a, b, c = (
    int(input('Masukkan angka A : ')),
    int(input('MAsukkana angka B : ')),
int(input('Masukkan angka C : '))
)

print('angka yang masuk : ', a, b, c)
if a > b and a > c:
    print('Nilai A paling besar yaitu :', a)
elif b > a and b > c:
    print('Nilai B paling besar yaitu : ', b)
else:
    print('Nilai C paling besar yaotu : ', c)