import requests
import xmltodict
import json
import pandas as pd
from datetime import datetime, timedelta
import glob

# 기준일자 시작과 끝 설정하기
start = "2021-01-01"
last = "2021-01-02"
start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")

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
        merge_df = pd.concat([merge_df, file_df], ignore_index=True)  # append -> concat으로 변경

    merge_df.to_excel(save_path, index=False)

# Open API를 호출하고 데이터를 엑셀로 저장
def fetch_and_save_data(start_date, last_date):
    key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
    rows = "100"
    
    # 날짜 범위 동안 데이터 처리
    while start_date <= last_date:
        dates = start_date.strftime("%Y%m%d")
        api_response = get_api_data(dates, page_no=1, rows=rows, key=key)

        total_count = int(api_response['responseXml']['header']['totalCount'])
        page_number = (total_count + int(rows) - 1) // int(rows)

        # 페이지 개수만큼 반복하여 데이터 수집
        for page in range(1, page_number + 1):
            print(f"\n날짜: {dates}, 페이지: {page}")
            api_response = get_api_data(dates, page_no=page, rows=rows, key=key)
            items = api_response['responseXml']['body']['item']

            if items:
                df = pd.DataFrame(items)
                df.to_excel(f"jeon_{dates}_{page}.xlsx", index=False)
        
        # 날짜를 하루씩 증가
        start_date += timedelta(days=1)

# 메인 실행(해당 파이썬을 직접 실행하면 __name__ 은 "__main__"이 됨)
if __name__ == "__main__":
    # 데이터 다운로드 및 엑셀 파일 저장
    fetch_and_save_data(start_date, last_date)
    
    # 다운로드한 엑셀 파일 병합
    merge_excel_files(file_path="./", save_path="./merged_data.xlsx")
