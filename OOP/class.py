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
    name = ''
    def get_name(self, isi_nama):
        self.name = isi_nama
        return self.name

akses = Pemain()
print(akses.get_name('Ronaldo'))
