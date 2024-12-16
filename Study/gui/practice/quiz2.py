def solution(price, grade):
    discount = {"S": 5, "G": 10, "V": 15}
    return int(price - (price * discount[grade] / 100))

# 예시1
price1 = 2500
grade1 = "V"

# 예시2
price2 = 96900
grade2 = "S"

print(solution(price1, grade1), "원")
print(solution(price2, grade2), "원")