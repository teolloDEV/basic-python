# menggunakan list
panjang = int(input('Masukkan panjanf deret :  '))
fibonanci = [0, 1]

for i in range(2, panjang):
    index1 = fibonanci[i - 2]
    index2 = fibonanci[i - 1]

    angkaSelanjutnya = index1 + index2
    fibonanci.append(angkaSelanjutnya)

print(fibonanci)

# Menggunakan variabel bantuan

panjang2 = int(input('Masukkan panjang deret : '))
angka1, angka2 = 0, 1
for i in range(panjang2):
    print(f'perulangan ke - {i}')