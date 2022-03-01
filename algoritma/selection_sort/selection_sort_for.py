def selection_sort(data):
    for i in range(len(data) - 1):
        index = i
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                index = j

        temp = data[i]
        data[i] = data[index]
        data[index] = temp
    print('iterasi ', i, data)


data = [4, 3, 5, 6, 2, 78, 98]
selection_sort(data)
