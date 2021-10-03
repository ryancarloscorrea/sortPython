def numTamanho(n):
    return len(str(n))


def countingSort(inputArray, placeValue):
    count = [0] * 10
    for i in range(len(inputArray)):
        placeElement = (inputArray[i] // placeValue) % 10
        count[placeElement] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    outputArray = [0] * len(inputArray)
    for i in range(len(inputArray) - 1, -1, -1):
        placeElement = (inputArray[i] // placeValue) % 10
        outputArray[count[placeElement] - 1] = inputArray[i]
        count[placeElement] -= 1
    return outputArray


def radixSort(inputArray):
    maxElement = max(inputArray)
    num_digits = len(str(maxElement))
    placeValue = 1
    outputArray = inputArray
    for d in range(num_digits):
        outputArray = countingSort(outputArray, placeValue)
        placeValue *= 10
    return outputArray
