def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 중간 값을 피벗으로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 값들을 모은 서브 배열
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 값들을 모은 서브 배열
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값들을 모은 서브 배열
    return quick_sort(left) + middle + quick_sort(right)  # 재귀적으로 정렬 후 결합

# 예시 사용법
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # 출력: [1, 1, 2, 3, 6, 8, 10]