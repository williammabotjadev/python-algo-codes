# Python merge sort implementation

def mergesort(arr):

    # Base Case 

    if len(arr) <= 1:
        return 

    # Find the Mid point

    mid = int(len(arr)//2)

    # Partition the main array 

    left = arr[:mid]
    right = arr[mid:]

    # Recursively run mergesort on each side

    mergesort(left)
    mergesort(right)

    # Swap items based size on either sides 

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1 

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1 

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1 

    return arr 

import random

if __name__ == "__main__":
    
    # Test Cases
    lst = []

    for i in range(100):
        num = random.randint(1, 100)
        if num not in lst:
            lst.append(num)

    print("Random Array: ")
    print(lst)
    result = mergesort(lst)
    print("Sorted Array: ")
    print(result)


