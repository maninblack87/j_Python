import pandas as pd

# Excel 파일 경로
excel_file = 'D:\Jeon\python\jeon\withExcel\sample\sample.xlsx'

# Excel 파일의 첫 번째 시트 읽기
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# 데이터프레임 출력
print(df)