from insertion_sort import insertion_sort
from MergeSort import mergeSort
from selectionSort import selectionSort
from RadixSort import radixSort
from shellSort import shellSort
from HeapSort import heapSort

import timeit
import numpy as np
import pandas as pd

from src.algorithmsSort.graph import generateGraph


def execFuncSort(index, arr):

    if index == 0:
        selectionSort(arr)
    elif index == 1:
        insertion_sort(arr)
    elif index == 2:
        mergeSort(arr)
    elif index == 3:
        heapSort(arr)
    elif index == 4:
        shellSort(arr)
    else:
        radixSort(arr)




if __name__ == '__main__':

    inc = 1000
    print("Escolha o valor maxímo de entrada: minimo (2000) maximo (20000)")
    max = int(input())
    stp = 1000
    rpt = 1

    numLoops = int(max / stp)
    numbersN = []

    meanOfTimes = np.array([[]])

    listOfSorts = ["SELECTION", "INSERTION", "MERGE", "HEAP", "SHELL", "RADIX"]

    # array dos N valores
    for x in (range(numLoops)):
        n = inc * (x + 1)
        numbersN.append(n)

    listMeanTimes = []

    # init table
    table = pd.DataFrame(index=numbersN, columns=listOfSorts)

    # laço inicial para cada valor de entrada
    for idx, n in enumerate(numbersN):
        print('valor de n: ', n)
        list_of_times = []
        # laço para cada algoritmo
        for indexAlg, algSort in enumerate(listOfSorts):
            # laço para repetir o algoritmo de ordenação
            for x in range(rpt):
                start = timeit.default_timer()

                arr = np.random.randint(0, 10000, n)
                execFuncSort(indexAlg, arr)

                final = timeit.default_timer()

                time = final - start
                list_of_times.append(time)

            #calcula média dos tempos de exução (do laço acima)
            media_time = np.mean(list_of_times)
            listMeanTimes.append(media_time)
            list_of_times.clear()

            ### array of array times to aux craete table
            if algSort == "SELECTION":
                meanOfTimes = np.array([[round(media_time, 4)]])
            else:
                meanOfTimes = np.concatenate((meanOfTimes, np.array([[round(media_time, 4)]])))

        # GERANDO TABELA

            table.at[n, algSort] = float(meanOfTimes[indexAlg])
    print(table)
    generateGraph(table, numbersN, max)


