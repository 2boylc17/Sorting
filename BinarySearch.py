import math

arr = [173, 179, 271, 364, 382, 390, 453, 509, 515, 566, 649, 737, 758, 836, 929]
newarr = arr
found = False
searchValue = 737
start = 0
end = len(arr) - 1
while found is False:
    middle = math.floor((start + end) / 2)
    if newarr[middle] == searchValue:
        print(f"Found value {searchValue} at index {middle}")
        found = True
    elif newarr[middle] > searchValue:
        end = middle
    elif newarr[middle] < searchValue:
        start = middle
