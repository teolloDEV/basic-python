# melakukan iterasi tiap karakter

# teks = 'selamat pagi'
#
# for karakter in teks:
#     print(karakter)

#  latihan
# 1. meminta user memasukkan teks dan mengubahnya menjadi huruf kecil
# 2. Membuat variabel untuk menyimpan huruf vokal

teks = input('Tuliskan teks: ').lower()
huruf_vokal = {
  'a': 0,
  'i': 0,
  'u': 0,
  'e': 0,
  'o': 0
}
total_huruf_vokal = 0

for karakter in teks:
    if karakter in ['a', 'i', 'u', 'e', 'o']:
        huruf_vokal [karakter] += 1
        total_huruf_vokal += 1
print(f'Total karakter: {len(teks)}')
print(f'Total huruf vokal: {total_huruf_vokal}')
print(f"""\
  a -> {huruf_vokal['a']}
  i -> {huruf_vokal['i']}
  u -> {huruf_vokal['u']}
  e -> {huruf_vokal['e']}
  o -> {huruf_vokal['o']}\
""")