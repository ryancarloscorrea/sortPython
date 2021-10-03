def heap(arr, n, i):
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i

    if esquerda < n and arr[maior] < arr[esquerda]:
        maior = esquerda

    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heap(arr, n, maior)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heap(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
