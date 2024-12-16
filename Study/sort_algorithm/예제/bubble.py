def bubble_sort(arr):
    n = len(arr)
    
    # 모든 원소에 대해 반복
    for i in range(n):
        # 현재 인덱스 이후의 모든 원소에 대해 반복
        for j in range(0, n-i-1):
            # 현재 원소와 다음 원소를 비교하여 필요에 따라 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 예제 배열
arr = [64, 34, 25, 12, 22, 11, 90]

# 정렬 전 배열 출력
print("정렬 전 배열:", arr)

# 버블 정렬 수행
bubble_sort(arr)

# 정렬 후 배열 출력
print("정렬 후 배열:", arr)