import pandas as pd

# Excel 파일의 Sheet1 읽기
excel_file = 'withExcel\practice\sample.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1')

print(df)