panjang = int(input('Masukkan panjang deret: '))

fibonanci = [0,1]

for i in range(2, panjang):
    angka1 = fibonanci[i - 2]
    angka2 = fibonanci[i - 1]
    angka_selanjutnya = angka1 + angka2
    fibonanci.append(angka_selanjutnya)
print(fibonanci)