def bubble_sort(lista):
    
    lista_sort = lista

    for posição in range (len(lista) - 1):
        for comparar in range(len(lista) - 1):
            if lista_sort[comparar] > lista_sort[comparar + 1]:
                lista_sort[comparar], lista_sort[comparar + 1] = lista_sort[comparar + 1], lista_sort[comparar]

    return lista_sort

lista = [10, 2, 5, 100, 895, -1, -500, 1, 250]

print(bubble_sort(lista))