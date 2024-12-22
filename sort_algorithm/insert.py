def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
# 예제 배열
arr = [6, 3, 2, 1, 4, 5, 9]
# 삽입정렬 호출
insertion_sort(arr)
print(arr)