def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    ############################
    # 여기에 코드를 작성하세요. #
    
    # 반복문으로 1월 1일 부터 month월 까지의 일수를 구한다
    for i in range(month-1):
        total += month_list[i]
        
    # 거기에 day를 더한다
    total += day
    
    ############################
    return total - 1
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total


# 예제
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("Solution: return value of the function is", ret, ".")