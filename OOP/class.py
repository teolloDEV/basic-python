# membuat class

# cara 1

class Mobil:
    name = 'BMW'
    def get_name(self):
        return self.name
akses = Mobil()
print(akses.name)

# cara 2

class Pemain:

    #name dibuat abstracat
    name = ''
    def get_name(self, isi_nama):
        self.name = isi_nama
        return self.name
# satu kelas bisa di panggil oleh banyak object
pemain_manchester = Pemain()
pemain_psg = Pemain()
print(pemain_manchester.get_name('Ronaldo'))
print(pemain_psg.get_name('mbappe'))
