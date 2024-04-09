def solution(people, limit):
    # 조건1 : boat에는 2개의 people[x]만 들어갈 수 있다
    # 조건2 : boat[0]과 boat[1]의 합 <= 매개변수 limit 이어야 한다
    # >> 조건 명세 : boat에 limit 값에 가장 근접한 people[x] + people[y]를 우선적으로 태워서 효율을 최대화 해보자
    # ! 참고 ! 여기서 일반적으로 ______remove()함수_______는 people 중에 사람을 구명 보트에 태워보낸다는 의미이다
    
    # answer는 구명 보트에 태워보낸 횟수를 의미한다
    answer = 0
    
    # people 리스트를 내림차순으로 정렬한다
    people.sort(reverse=True)
    
    # 반복문
    while True:
        # 만약 people이 2명 이상 남았다면 아래 조건문에 따라 태워보낸다
        if len(people) > 1:
            # 조건문 : 둘 혹은 하나만 태워 보낸다
            # 만약 : limit - people[0]의 이하 값이 1개 이상 있으면
            # >> 그 중, 가장 큰 값을 태워보낸다
            if len(list(filter(lambda x : x <= (limit-people[0]), people))) > 0 :
                people.remove(people[0])
                people.remove(max(filter(lambda x : x <= (limit-people[0]), people)))
                answer = answer + 1
            # 그 외에는: people[0]만 태워보낸다
            else:
                people.remove(people[0])
                answer = answer + 1
        # 그렇지 않고, people이 단 1명 남았다면 해당 사람만 태워보내고 탈출한다!
        elif len(people) == 1:
            people.remove(people[0])
            answer = answer + 1
            break
        # 만약, 모든 people이 구명 보트에 태워져 나갔다면 반복문을 탈출한다!
        else:
            break
            
    # 최소한의 탑승 횟수(count)로 해결해야 한다
    return answer


print(solution([70, 50, 80, 50], 100))
print("\n\n----------------------------------\n\n")
print(solution([70, 80, 50], 100))