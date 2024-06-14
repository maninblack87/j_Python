import pandas as pd
import os

# 파일 경로를 정확하게 지정합니다.
file_path = 'D:\Jeon\python\jeon\gui\excel\sample.xlsx'

# 파일이 존재하는지 확인
if os.path.exists(file_path):
    try:
        # Excel 파일 읽기
        df = pd.read_excel(file_path)
        
        # 데이터프레임 내용 확인
        print("데이터프레임 내용:")
        print(df.head())  # 처음 다섯 행 출력
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
else:
    print(f"파일을 찾을 수 없습니다: {file_path}")