def solution(shirt_size):
    answer = []
    size   = ["XS", "S", "M", "L", "XL", "XXL"]
    for i in size:
        answer.append(shirt_size.count(i))
    return answer
        
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
print(solution(shirt_size))