import tkinter as tk
import pandas as pd

# 엑셀 파일에서 데이터프레임으로 데이터 읽기
excel_file = 'withExcel\practice\sample.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# tkinter 창 생성
root = tk.Tk()
root.title("Excel 데이터 표시")
root.geometry("600x400")

# 레이블 생성
for i in range(0, 5):
    frame = tk.Frame()
    for j in range(0, 3):
        anyword = tk.StringVar(value=df.iloc[i, j])
        output_name = tk.Entry(frame, width='10', state='readonly' ,textvariable=anyword)
        output_name.pack(side='left')

# 이벤트 루프 시작
root.mainloop()