import json

# JSON 파일 경로
file_path = 'foods.json'

# JSON 파일 불러오기
with open(file_path, 'r') as file:
    data = json.load(file)

# 불러온 데이터 출력
print(data)



# ######## 파일을 못 찾겠다고 해서 잠정적 포기