def selectionSort(vetoRecebido):
    tamanho = len(vetoRecebido)

    for item in range(tamanho):
        menor = item

        for i in range(item + 1, tamanho):
            if vetoRecebido[i] < vetoRecebido[menor]:
                menor = i

        (vetoRecebido[item], vetoRecebido[menor]) = (
            vetoRecebido[menor], vetoRecebido[item])


numbers = [73, 62, 61, 69]
selectionSort(numbers)
print("Sorted list:", numbers)
