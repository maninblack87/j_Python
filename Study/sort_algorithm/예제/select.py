def selection_sort(arr):
    n = len(arr)
    
    # 배열의 모든 원소에 대해 반복
    for i in range(n):
        # 현재 인덱스부터 배열 끝까지의 최솟값을 찾음
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # 최솟값을 현재 인덱스로 이동
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 예제 배열
arr = [64, 34, 25, 12, 22, 11, 90]

# 정렬 전 배열 출력
print("정렬 전 배열:", arr)

# 선택 정렬 수행
selection_sort(arr)

# 정렬 후 배열 출력
print("정렬 후 배열:", arr)