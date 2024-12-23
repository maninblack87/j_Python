import tkinter as tk
from tkinter import ttk

from modules import select_output_folder

# Tkinter GUI 구성
root = tk.Tk()
root.title("Open API 데이터 다운로드")

# 시작일자 구성
# 1. 시작일자 레이블(0행 0열)
tk.Label(root, text="시작일자 (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
# 2. 시작일자 엔트리(0행 1열)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1, padx=10, pady=5)

# 종료일자 구성
# 1. 종료일자 레이블(1행 0열)
tk.Label(root, text="종료일자 (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
# 2. 종료일자 엔트리(1행 1열)
last_date_entry = tk.Entry(root)
last_date_entry.grid(row=1, column=1, padx=10, pady=5)

# 인증키 입력 구성
# 1. 인증키 입력 레이블(2행 0열)
tk.Label(root, text="API 키:").grid(row=2, column=0, padx=10, pady=5)
# 2. 인증키 입력 엔트리(2행 1열)
api_key_entry = tk.Entry(root)
api_key_entry.grid(row=2, column=1, padx=10, pady=5)

# 출력 폴더 선택 구성
# 1. 출력폴더 레이블(3행 0열)
tk.Label(root, text="출력 폴더").grid(row=3, column=0, padx=10, pady=5)
# 2. 출력폴더 경로의 변수 생성(빈 문자열의 상태로)
output_dir_var = tk.StringVar();
# 함수. 출력폴더 선택 후, 경로를 out_dir_var에 설정하는 함수
def on_folder_selected():
    # 폴더를 선택하는 select_output_folder()함수를 호출
    path = select_output_folder.select_output_folder()
    # 이에 폴더가 선택되었다면 output_dir_var에 설정한다
    if path:
        output_dir_var.set(path)
# 3. 출력폴더 버튼(3행 1열)
output_dir_button = tk.Button(root, text="폴더 선택", command=on_folder_selected)
output_dir_button.grid(row=3, column=1, padx=10, pady=5)

# 진행 상태 표시 구성
# 1. 진행 상태를 계량하는 변수 생성(빈 값의 상태로)
progress_var = tk.DoubleVar()
# 2. 진행 상태를 표시하는 바를 생성(4행 0~1열)
progress_bar = ttk.Progressbar(root, length=300, variable=progress_var, maximum=100)
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# 다운로드 시작 버튼 구성
start_button = tk.Button(root, text="다운로드 시작", command=곧 작업합니다)