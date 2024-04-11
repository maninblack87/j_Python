def insertion_sort(arr):
    n = len(arr)
    
    # 배열의 두 번째 원소부터 시작하여 마지막 원소까지 반복
    for i in range(1, n):
        # 현재 원소를 정렬된 부분에 삽입하기 위해 이전 원소와 비교
        key = arr[i]
        j = i - 1
        
        # 이전 원소와 비교하면서 적절한 위치에 삽입
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(f"i = {i}, j = {j} ,arr = {arr}")
            j -= 1
        
        # 삽입할 위치에 현재 원소 삽입
        arr[j + 1] = key
        print(f"{i}번째 : {arr}")

# 예제 배열
arr = [64, 34, 25, 12, 22, 11, 90]

# 정렬 전 배열 출력
print("정렬 전 배열:", arr)

# 삽입 정렬 수행
insertion_sort(arr)

# 정렬 후 배열 출력
print("정렬 후 배열:", arr)