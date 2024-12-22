# 배열에 들어있는 숫자들의 개수를 카운팅하고 배열로 반환하는 함수(숫자 1001까지)
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter
 
# 배열에서 최대 값을 반환하는 함수
def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

# 배열에서 최소 값을 반환하는 함수
def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    # 아래 부분 주석을 해제하고, @를 올바르게 수정해 주세요.
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("Solution: return value of the function is", ret, ".")