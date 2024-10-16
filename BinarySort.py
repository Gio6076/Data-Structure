def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
print("This is the Unsorted Array:", arr)

bubble_sort(arr)
print("This is the Sorted Array:", arr)

target = int(input("What number are you looking for: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Number {target} is found at index {result}")
else:
    print(f"Number {target} is not found in the array")
