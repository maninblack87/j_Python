def solution(arr):
    left, right = 0, len(arr)-1
    ###########################
    # 여기에 코드를 작성하세요. #
    
    for i in range(len(arr)//2):
        
        # arr[left]와 arr[right] 스왑
        tmp        = arr[left]
        arr[left]  = arr[right]
        arr[right] = tmp
        
        # arr[left] 인덱스 +1 이동
        # arr[right] 인덱스 -1 이동
        left  += 1
        right -= 1
    
    ###########################
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("Solution: return value of the function is ", ret, " .")