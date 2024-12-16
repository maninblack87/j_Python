from math import isqrt

def solution(n, k):
    answer = 0
    
    kin = ''
    while n:
        kin = kin + str(n % k)
        n = n // k
    kin = kin[::-1]
    
    arr = list(kin.split('0'))
    
    # 체크 반복문
    for a in arr:
        # 리스트 arr의 원소가 ''이거나 '1'이면 즉시 다음 원소를 체크한다
        if (a == '') or (a == '1'): continue
        
        # 소수 판별을 위한 플래그 변수
        is_prime = True
        
        # 2차 반복문
        for i in range(2, isqrt(int(a)) + 1):
            if int(a) % i == 0:
                is_prime = False
                break
        
        # 소수인 경우 결과값에 +1
        if is_prime:
            answer += 1
    
    return answer