# Predikat A untuk nilai >= 90
# Predikat B untuk nilai >= 80 < 90
# Predikat C untuk nilai >= 60 < 80
# Predikat D untuk nilai >= 40 < 60
# Selain itu, maka predikat E.

nilai = int(input('Masukkan nilai : '))

if nilai >= 90:
    print('Predikat anda A ')
elif nilai >= 80 < 90:
    print('predikat anda B ')
elif nilai >= 60 < 80:
    print('Predikat anda C ')
elif nilai >= 40 < 60:
    print('Predikat anda D')
else:
    print('Predikat anda E')