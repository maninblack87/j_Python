import pandas as pd

# Excel 파일 경로
excel_file = 'D:\Jeon\python\jeon\withExcel\sample\sample.xlsx'

# Excel 파일의 첫 번째 시트에서 데이터프레임으로 데이터 읽기
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# 2행 2열의 데이터 출력
data = df.iloc[0, 0]  # 1행 1열의 데이터 (0-based index)

print("Sheet1의 2행 2열 데이터:", data)