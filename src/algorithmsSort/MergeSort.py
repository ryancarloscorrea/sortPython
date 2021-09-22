def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        lowToMid = arr[:mid]

        midToHigh = arr[mid:]

        mergeSort(lowToMid)
        mergeSort(midToHigh)

        i = j = k = 0

        while i < len(lowToMid) and j < len(midToHigh):
            if lowToMid[i] < midToHigh[j]:
                arr[k] = lowToMid[i]
                i += 1
            else:
                arr[k] = midToHigh[j]
                j += 1
            k += 1

        while i < len(lowToMid):
            arr[k] = lowToMid[i]
            i += 1
            k += 1

        while j < len(midToHigh):
            arr[k] = midToHigh[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr)
    print("Array ordenado: ")
    printList(arr)
