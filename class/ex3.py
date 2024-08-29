import tkinter as tk
from functools import partial

def add_numbers(num1, num2):
    try:
        # 두 숫자를 더합니다.
        result = int(num1) + int(num2)
        # 결과를 레이블에 표시합니다.
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # 잘못된 입력이 들어올 경우 처리합니다.
        result_label.config(text="Please enter valid numbers")

# 메인 윈도우 생성
root = tk.Tk()
root.title("계산기")

# 첫 번째 숫자 입력 필드
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# 두 번째 숫자 입력 필드
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# "Add" 버튼, functools.partial을 사용하여 add_numbers에 인자를 전달
add_button = tk.Button(
    root,
    text="Add",
    command=partial(add_numbers, entry1.get, entry2.get)
)
add_button.pack(pady=10)

# 결과를 표시할 레이블
result_label = tk.Label(root, text="결과: ")
result_label.pack(pady=10)

# GUI 애플리케이션 실행
root.mainloop()