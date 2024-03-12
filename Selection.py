def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr =[45, 37, 22, 92, 0, 10, 90]

print("Original array:")
print(*arr)

selection_sort(arr)

print("Sorted array:")
print(*arr)
