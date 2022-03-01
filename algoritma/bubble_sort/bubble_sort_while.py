data = [5, 6, 3, 1, 2, 9, 10]
print(data)

i = 0
j = len(data) - 1

while (i != j):
    index = i
    for x in range (i+1, j+1):
        if data[x] < data[index]:
            index = x
    temp = data[index]
    data[index] = data[i]
    data[i] = temp

    i = i+1
    print(data)

