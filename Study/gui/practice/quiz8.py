def solution(sentence):
    # 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True

sentence1 = "never odd or even."
ret1 = solution(sentence1)

print("Solution: return value of the function is", ret1, ".")
    
sentence2 = "palindrome"
ret2 = solution(sentence2)

print("Solution: return value of the function is", ret2, ".")