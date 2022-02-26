def sequential_search(data, search):
    index = len(data)
    value = False
    data1 = []

    for i in range(0, index):
        if search == data[i]:
            value = True
            data1.append(i)

    if value == True:
        print("data found")
        for i in data1:
            print("in index : ", i)
    else:
        print("data not found")


data = [1, 33, 55, 66, 77, 33, 100]
print("Data : ", data)

search = int(input("What data are you looking for : "))
sequential_search(data, search)
