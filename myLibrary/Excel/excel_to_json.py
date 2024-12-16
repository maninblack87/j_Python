import pandas as pd
import json

def xlsx_to_json(file_name):
    
    # 1. 엑셀 파일 읽기(데이터 프레임화)
    df = pd.read_excel(file_name)

    # 2. 데이터 프레임을 리스트로 변환
    data = df.to_dict(orient='recordes')

    # 3. JSON 파일로 저장
    with open(file_name[:-5] + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)