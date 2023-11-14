arr = [649, 929, 179, 382, 509, 758, 737, 271, 390, 566, 515, 173, 836, 453, 364]
swapped = False
num = len(arr)
while swapped is False:
    swapped = True
    for count in range(0, num - 1):
        if arr[count] == arr[num - 1]:
            pass
            print("complete")
        elif arr[count] > arr[count + 1]:
            arr[count], arr[count + 1] = arr[count + 1], arr[count]
            swapped = False
    print(arr)
