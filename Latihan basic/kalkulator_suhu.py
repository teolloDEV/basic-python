print("==========PROGRAM KONVERSI SUHU============")

indeks = {
    "Celcius    ": "c",
    "Reamur     ": "r",
    "Fahrenheit ": "f",
    "Kelvin     ": "k"
}

print("==========Index Satuan Skala Suhu==========\n")
for i in indeks:
    print("Satuan suhu : ", i, "\t Indeks : ", indeks[i])

suhu = float(input("Masukkan  Suhu : "))
satuan = input("Masukkan index satuan skala suhu : ")

if (satuan == "c"):
    print("Suhu yang anda masukkan adalah ", suhu, "derajat celcius")
    print("Reamur = ", (suhu*4/5), "derajat")
    print("Fahrenheit = ", (suhu*9/5)+32, "derajar")
    print("Kelvin = ", (suhu + 273), "derajat")
elif (satuan == "r"):
    print("Suhu yang anda masukkan adalah ", suhu, "derajat reamur")
    print("Celcius = ", (suhu*5/4), "derajat")
    print("Fahrenheit = ", (suhu*9/4)+32, "derajar")
    print("Kelvin = ", (suhu * 5/4) +273, "derajat")
elif (satuan == "f"):
    print("Suhu yang anda masukkan adalah ", suhu, "derajat fahrenheit")
    print("Celcius = ", (5/9)*(suhu-32), "derajat")
    print("Reamur = ", (4/9)*(suhu-32), "derajar")
    print("Kelvin = ", (5/9)*(suhu-32)+273, "derajat")
elif (satuan == "k"):
    print("Suhu yang anda masukkan adalah ", suhu, "derajat kelvin")
    print("Celcius = ", suhu-273, "derajat")
    print("Reamur = ", (4/5)*(suhu-273), "derajar")
    print("Fahreinheit = ", (9/5)*(suhu-273)+32, "derajat")
else:
    print("indeks yang anda masukkan tidak ada")

