import pandas as pd

# 데이터프레임 생성
data = {'이름': ['John', 'Anna', 'Peter', 'Linda'],
        '나이': [25, 35, 30, 28],
        '성별': ['남', '여', '남', '여']}

df = pd.DataFrame(data)

# 데이터프레임 출력
print("데이터프레임:")
print(df)
print()

# 특정 열 선택
print("이름 열 선택:")
print(df['이름'])
print()

# 특정 행 선택
print("첫 번째 행 선택:")
print(df.iloc[0])
print()

# 특정 조건으로 행 선택
print("나이가 30 이상인 행 선택:")
print(df[df['나이'] >= 30])
print()

# 통계 정보 출력
print("통계 정보:")
print(df.describe())



