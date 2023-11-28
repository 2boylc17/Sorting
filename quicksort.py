def partition(data, start, end):
    i = start
    j = end
    pivot = data[(start+end)//2]
    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        else:
            return j


def quicksort(data, start, end):
    if end <= start:
        return "List sorted"
    else:
        print(data, start, end)
        pivot = partition(data, start, end)
        quicksort(data, start, pivot - 1)
        quicksort(data, pivot + 1, end)


list1 = [47, 36, 14, 21, 91, 18, 17, 82, 84, 6, 73]
quicksort(list1, 0, len(list1) - 1)
