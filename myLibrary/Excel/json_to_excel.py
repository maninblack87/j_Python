import pandas as pd
import json

def json_to_xlsx(file_name):

    # 1. JSON파일 읽기
    with open(file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # 2. 데이터프레임으로 변환
    df = pd.json_normalize(data)

    # 3. 엑셀로 저장
    df.to_excel(file_name[:-5] + '.xlsx', index=False)


# 테스트
from excel_to_json import xlsx_to_json

# file_name = 'C:/jeon/j_Python/test/test.xlsx'
# xlsx_to_json(file_name)

file_name = 'C:/jeon/j_Python/test/test.json'
json_to_xlsx(file_name)