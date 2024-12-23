# 폴더 선택하는 대화상자를 생성하는 함수
import tkinter as tk
from tkinter import filedialog

def select_output_folder():
    # 1. 폴더를 선택할 수 있는 다이얼로그를 열어줌
    folder_selected = filedialog.askdirectory()
    # 2. 다이얼로그에서 선택한 폴더를 반환한다
    return folder_selected