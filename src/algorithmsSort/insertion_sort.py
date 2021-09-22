def insertion_sort(vetoRecebido):

    for index in range(1, len(vetoRecebido)):
        valorAtual = vetoRecebido[index]
        posicaoAtual = index

        while posicaoAtual > 0 and vetoRecebido[posicaoAtual - 1] > valorAtual:
            vetoRecebido[posicaoAtual] = vetoRecebido[posicaoAtual - 1]
            posicaoAtual = posicaoAtual - 1

        vetoRecebido[posicaoAtual] = valorAtual


array = [4, 22, 41, 40, 27, 30, 36, 16, 42,
         37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertion_sort(array)
print(array)
