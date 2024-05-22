## 목표 : 엑셀 파일에서 1행 1열의 데이터를 출력한다 ##
import pandas as pd
df = pd.read_excel('sample.xlsx')
data = df.iloc[0, 0]
print("1행 1열의 데이터:", data)