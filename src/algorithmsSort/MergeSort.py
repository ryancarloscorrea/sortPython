def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        initToMid = arr[:mid]

        midToFinal = arr[mid:]

        mergeSort(initToMid)
        mergeSort(midToFinal)

        i = j = k = 0

        while i < len(initToMid) and j < len(midToFinal):
            if initToMid[i] < midToFinal[j]:
                arr[k] = initToMid[i]
                i += 1
            else:
                arr[k] = midToFinal[j]
                j += 1
            k += 1

        while i < len(initToMid):
            arr[k] = initToMid[i]
            i += 1
            k += 1

        while j < len(midToFinal):
            arr[k] = midToFinal[j]
            j += 1
            k += 1
