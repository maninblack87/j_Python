def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        #  j는 i-1부터 시작해서 0까지 반복문 수행
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            