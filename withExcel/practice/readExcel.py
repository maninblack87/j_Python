import pandas as pd

# Excel 파일 경로로 해당 파일의 첫 번째 시트 읽기
excel_file = 'withExcel\practice\sample.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# 출력
print(df)