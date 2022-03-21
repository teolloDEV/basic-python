panjang = int(input('Masukkan panjang deret : '))
angka1, angka2 = 0, 1
for i in range(panjang):
    if (i < 2):
        print(i)
    else:
       angka_sekarang = angka1 + angka2
       print(angka_sekarang)
       angka1 = angka2
       angka2 = angka_sekarang
