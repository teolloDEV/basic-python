def cek_bilangan_prima(x):
    for i in range(2, x):
        if x % 2 == 0:
            return  False
    return True
print(cek_bilangan_prima(20))
