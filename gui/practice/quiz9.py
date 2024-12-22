def solution(characters):
    result = ""
    result += characters[0]
    for i in range(len(characters)):
        ############################
        # 여기에 코드를 작성하세요. #
        if result[-1] != characters[i]:
            result += characters[i]
        ############################
    return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print("Solution: return value of the function is", ret, ".")