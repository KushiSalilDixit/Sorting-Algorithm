def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [45, 37, 22, 92, 0, 10, 90]
bubble_sort(arr)
print("Sorted array:")
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
