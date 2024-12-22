import tkinter as tk

def button_click(button_id):
    print("버튼", button_id, "이(가) 클릭되었습니다!")

# tkinter 윈도우 생성
window = tk.Tk()
window.title("반복문으로 생성된 버튼 속성 수정하기")

# 버튼을 생성하고 배치하는 반복문
buttons = []  # 버튼들을 담을 리스트
for i in range(1, 6):
    if i == 2:
        button_text = "다른 텍스트"
        button_bg = "yellow"  # 두 번째 버튼의 배경색을 변경
    else:
        button_text = "버튼 " + str(i)
        button_bg = "lightgray"
    button = tk.Button(window, text=button_text, bg=button_bg, command=lambda idx=i: button_click(idx))
    button.pack()
    buttons.append(button)  # 생성된 버튼을 리스트에 추가

# 두 번째 버튼의 속성 수정
buttons[1]["text"] = "수정된 텍스트"
buttons[1]["bg"] = "green"

# 이벤트 루프 시작
window.mainloop()