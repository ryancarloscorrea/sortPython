def insertion_sort(vetoRecebido):

    for index in range(1, len(vetoRecebido)):
        valorAtual = vetoRecebido[index]
        posicaoAtual = index

        while posicaoAtual > 0 and vetoRecebido[posicaoAtual - 1] > valorAtual:
            vetoRecebido[posicaoAtual] = vetoRecebido[posicaoAtual - 1]
            posicaoAtual = posicaoAtual - 1

        vetoRecebido[posicaoAtual] = valorAtual

