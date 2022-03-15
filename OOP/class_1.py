# Membuat class sebagai definisi
class Mobil:
    warna = None
    jenis = None

# membangun instance sebagai object nyata

mobil1 = Mobil()
mobil1.warna = 'Merah'
mobil1.jenis = 'Mobil Sport'

mobil2 = Mobil()
mobil2.warna = 'Biru'
mobil2.jenis = 'Mobil Travel'

# menampilkan masing - masing atribut

print(mobil1.jenis, mobil2.warna)
print(mobil2.jenis, mobil1.warna)

