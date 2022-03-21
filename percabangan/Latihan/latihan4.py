# cek dan tampilkan list bilangan genap atau ganjil dari range

print('Masukkan nilai awal dan akhir')

nilai_awal = int(input('Masukkan nilai awal : '))
nilai_akhir = int(input('Masukkan nilai akhir : '))

print('''
Tampilkan bilangan : \n 1. ganjil \n 2. genap
''')
pilihan = int(input('Masukkan pilihan anda : '))

if pilihan not in [1, 2] :
    print('Maaf pilihan anda tidak ada')
else:
    for x in range(nilai_awal, nilai_akhir + 1):
        if pilihan == 1 and x % 2 == 1:
            print(x, end=' ')
        elif pilihan == 2 and x % 2 == 0:
            print(x, end=' ')

    else:
    # ganti baris ketika perulangan selesai
       print('')
       print(x, end=' ')