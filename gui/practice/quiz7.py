def solution(scores):
    # 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print("Solution: return value of the function is", ret, ".")