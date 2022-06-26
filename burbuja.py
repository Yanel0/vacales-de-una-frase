def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
