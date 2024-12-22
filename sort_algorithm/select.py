def selection_sort(arr):
    n = len(arr)    # arr의 배열의 길이
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]     # 최소값을 현재 인덱스로 이동
        
arr = [64, 34, 25, 12, 22, 11, 90]

selection_sort(arr)
print(arr)