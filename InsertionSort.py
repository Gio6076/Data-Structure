def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

us = int(input("How many numbers? "))
arr = []
for i in range(us):
    num = int(input("Enter a number: "))
    arr.append(num)

insertionSort(arr)
print("Sorted numbers:")
printArray(arr)
