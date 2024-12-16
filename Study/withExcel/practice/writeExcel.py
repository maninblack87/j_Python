import pandas as pd

# 데이터 프레임 만들기
data = {
    '이름' : ['전석환1', '전석환2', '전석환3', '전석환4', '전석환5'],
    '나이' : [37, 37, 37, 37, 37],
    '성별' : ['남', '남', '남', '남', '남']
}
df = pd.DataFrame(data)

# 데이터 프레임을 Excel로 저장
excel_file = 'withExcel\practice\sample.xlsx'
df.to_excel(excel_file, index=False)

print(f"Excel 파일이 아래 경로로 저장되었습니다\n저장된 경로: {excel_file}")