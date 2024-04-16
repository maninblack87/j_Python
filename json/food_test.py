import json

# json 불러온다
with open("foods.json", "r") as file:
    data = json.load(file)

# 내가 최근에 먹은 것
# .. 새우깡
recent = "새우깡"

# 새우깡의 가격을 알아보자
# for item in data['식사']:
#     if item['이름'] == recent:
#         recent_price = item['가격']
#         break
    
# print(f"내가 최근에 먹은 {recent}의 가격은 {recent_price}원 이다.")