def bubbleSort(arr):
    n = len(arr) - 1
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j+1] = arr[j + 1], arr[j]
        if not swapped:
            return
    return arr
# Driver code to test above
arr = [64, 34, 25, 12, 22, 90, 11]
# 25 12 22
# 11  12  22  25  34  64  90
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
