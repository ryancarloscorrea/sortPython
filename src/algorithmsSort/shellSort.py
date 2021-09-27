def shellSort(vetoRecebido):
    auxSublista = len(vetoRecebido)//2
    while auxSublista > 0:

        for startposicao in range(auxSublista):
            gap(vetoRecebido, startposicao, auxSublista)

        auxSublista = auxSublista // 2


def gap(vetoRecebido, start, gap):
    for i in range(start+gap, len(vetoRecebido), gap):

        valorAtual = vetoRecebido[i]
        posicao = i

        while posicao >= gap and vetoRecebido[posicao-gap] > valorAtual:
            vetoRecebido[posicao] = vetoRecebido[posicao-gap]
            posicao = posicao-gap

        vetoRecebido[posicao] = valorAtual

