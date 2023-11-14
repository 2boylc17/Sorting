arr = [649, 929, 179, 382, 509]
num = len(arr)
for count in range(num - 1, 0, -1):
    current = arr[count]
    x = 0
    for index in range(count + 1):
        if arr[index] > current:
            current = arr[index]
            x = index
    arr[count], arr[x] = arr[x], arr[count]
    print(arr)
