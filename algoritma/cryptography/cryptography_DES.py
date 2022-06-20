# 1. kita import terlebih dahulu

from Crypto.Cipher import  DES
from Crypto.Util.Padding import pad

# 2. Mulai Enkripsi

# 3. Kita tentuin dulu key atau kuncinya
# karena saya menggunkan binari maka saya akan kasih penanda ' B '
# pada kali ini saya menggunakan 8 blok zize untuk kuncinya

key = b'1n1Kunc1'

# 4. Kita buat sebuah deskripsi
data = b'ini akan saya enkripsi'

# 5. Menentukan BLOck_ZIZE
# saya menggunakan 32

BLOCK_SIZE = 32

#6. Selanjutnya kita buat variabel des
des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data, BLOCK_SIZE)
encrypt = des.encrypt(padded_text)

#7. kita cetak

print(encrypt)

# kita buat deskripsi

key = b'1n1Kunc1'
data = b'ini akan saya enkripsi'
des = DES.new(key, DES.MODE_ECB)
dcrypt = des.decrypt(encrypt)

print(dcrypt)

