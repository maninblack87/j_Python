def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            ############################
            # 여기에 코드를 작성하세요. 
            if current % 10 in [3,6,9]:
                print("짝", end='')
                count += 1
            current = current // 10
            ############################
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

number = 40
ret = solution(number)

print("Solution: return value of the function is", ret, ".")
