def partition(arr, start, end):
    pivo = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivo:
            high = high - 1

        while low <= high and arr[low] <= pivo:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quicksort(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)

if __name__ == '__main__':
    array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]

    quicksort(array, 0, len(array) - 1)
    print(array)

