def solution(data):
    
    total = sum(data)
    average =  total / len(data)
    cnt = 0
    ############################
    # 여기에 코드를 작성하세요. #
    for i in data:
        if i <= average:
            cnt += 1
    ############################
    return cnt


#The following is code to output testcase. The code below is correct and you shall correct solution function.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

print("Solution: return value of the function is", ret1, ".")
    
data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

print("Solution: return value of the function is", ret2, ".")