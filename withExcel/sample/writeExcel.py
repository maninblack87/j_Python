import pandas as pd

# 데이터프레임 생성
data = {
    '이름': ['홍길동', '김철수', '이영희', '전석환'],
    '나이': [30, 25, 28, 37],
    '성별': ['남', '남', '여', '남']
}
df = pd.DataFrame(data)

# Excel 파일로 저장
excel_file = 'D:\Jeon\python\jeon\withExcel\sample.xlsx'
df.to_excel(excel_file, index=False)

print("Excel 파일이 저장되었습니다.")