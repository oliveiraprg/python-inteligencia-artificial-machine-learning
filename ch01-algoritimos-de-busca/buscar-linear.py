def linearSearch(listData, value):
    index = 0
    while (index < len(listData) and listData[index] < value):
        index = index + 1
        if value == listData[index]:
            return f'Valor encontrado na posição {index}'
    if (index >= len(listData or listData[index] != value)):
        return -1
    return index


numero = 6
listaNumeros = [1, 2, 3, 5, 6, 7, 8, 9, 12, 33, 244]

print(linearSearch(listaNumeros, numero))