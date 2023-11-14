import math

arr = [173, 179, 271, 364, 382, 390, 453, 509, 515, 566, 649, 737, 758, 836, 929]
newarr = arr
found = False
print(arr)
searchValue = int(input("What number are you searching for?\n"))
start = 0
end = len(arr) - 1
while found is False:
    middle = math.floor((start + end) / 2)
    print(start, end, middle)
    if newarr[middle] == searchValue:
        print(f"Found value {searchValue} at index {middle}")
        found = True
    elif start == end:
        print(f"Value '{searchValue}' is not in the list")
        found = True
    elif newarr[middle] > searchValue:
        end = middle - 1
    elif newarr[middle] < searchValue:
        start = middle + 1
