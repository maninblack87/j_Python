def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
# 예제
arr = [6, 4, 1, 3, 2, 5, 9]
bubble_sort(arr)