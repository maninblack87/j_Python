import pandas as pd
import tkinter as tk
from tkinter import ttk
from pandastable import Table

# 엑셀 파일 경로
excel_file = 'D:\Jeon\python\jeon\withExcel\sample\sample.xlsx'

# 엑셀 파일에서 데이터프레임으로 데이터 읽기
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# tkinter 창 생성
root = tk.Tk()
root.title("Excel 데이터 표시")

# 데이터를 표시할 Frame 생성
frame = ttk.Frame(root)
frame.pack(pady=20)

# 데이터를 표시할 테이블 생성 (툴바와 상태 표시줄 숨기기)
table = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=False)
table.show()

# tkinter 창 실행
root.mainloop()