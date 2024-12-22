import requests
import xmltodict
import pandas as pd
from datetime import datetime, timedelta
import glob
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# API 호출 함수
def get_api_data(base_dt, page_no=1, rows="100", key=None):
    url = f"http://apis.data.go.kr/1192000/select0040List/getselect0040List?serviceKey={key}&pageNo={page_no}&numOfRows={rows}&baseDt={base_dt}"
    response = requests.get(url)
    return xmltodict.parse(response.content)

# 엑셀 파일 병합 함수
def merge_excel_files(file_path, save_path, save_format=".xlsx"):
    merge_df = pd.DataFrame()
    file_list = glob.glob(f"{file_path}/*.xlsx")

    for file in file_list:
        file_df = pd.read_excel(file)
        merge_df = pd.concat([merge_df, file_df], ignore_index=True)

    merge_df.to_excel(save_path, index=False)

# 데이터 다운로드 및 엑셀로 저장
def fetch_and_save_data(start_date, last_date, api_key, output_dir, progress_var):
    rows = "100"
    
    # 날짜 범위 동안 데이터 처리
    while start_date <= last_date:
        dates = start_date.strftime("%Y%m%d")
        api_response = get_api_data(dates, page_no=1, rows=rows, key=api_key)

        total_count = int(api_response['responseXml']['header']['totalCount'])
        page_number = (total_count + int(rows) - 1) // int(rows)

        # 페이지 개수만큼 반복하여 데이터 수집
        for page in range(1, page_number + 1):
            api_response = get_api_data(dates, page_no=page, rows=rows, key=api_key)
            items = api_response['responseXml']['body']['item']

            if items:
                df = pd.DataFrame(items)
                df.to_excel(f"{output_dir}/jeon_{dates}_{page}.xlsx", index=False)

            # 진행 상태 업데이트
            progress_var.set(int(page / page_number * 100))
            root.update()  # GUI 업데이트

        # 날짜를 하루씩 증가
        start_date += timedelta(days=1)

# GUI 구성
def start_download():
    start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
    last_date = datetime.strptime(last_date_entry.get(), "%Y-%m-%d")
    api_key = api_key_entry.get()
    output_dir = output_dir_var.get()

    # 다운로드 및 엑셀 병합
    fetch_and_save_data(start_date, last_date, api_key, output_dir, progress_var)
    
    # 엑셀 파일 병합
    merge_excel_files(file_path=output_dir, save_path=f"{output_dir}/merged_data.xlsx")
    progress_var.set(100)  # 완료 후 100%로 설정

# 폴더 선택 대화상자
def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_dir_var.set(folder_selected)

# Tkinter GUI 구성
root = tk.Tk()
root.title("Open API 데이터 다운로드")

# 시작일자
tk.Label(root, text="시작일자 (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1, padx=10, pady=5)

# 종료일자
tk.Label(root, text="종료일자 (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
last_date_entry = tk.Entry(root)
last_date_entry.grid(row=1, column=1, padx=10, pady=5)

# API 키 입력
tk.Label(root, text="API 키:").grid(row=2, column=0, padx=10, pady=5)
api_key_entry = tk.Entry(root)
api_key_entry.grid(row=2, column=1, padx=10, pady=5)

# 출력 폴더 선택
tk.Label(root, text="출력 폴더:").grid(row=3, column=0, padx=10, pady=5)
output_dir_var = tk.StringVar()
output_dir_button = tk.Button(root, text="폴더 선택", command=select_output_folder)
output_dir_button.grid(row=3, column=1, padx=10, pady=5)

# 진행 상태 표시
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, length=300, variable=progress_var, maximum=100)
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# 다운로드 시작 버튼
start_button = tk.Button(root, text="다운로드 시작", command=start_download)
start_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# GUI 실행
root.mainloop()
