from tkinter import *
# 메서드 생성 : 버튼을 클릭했다고 출력해주는
def button_click(idx):
    if idx == 4:
        buttons[idx-1]["text"] = "클릭하면 변함"
        buttons[idx-1]["bg"]   = "white"
    print(f"버튼 {idx}가 클릭되었습니다.")
    
# 윈도우 생성
window = Tk()
window.title("반복문으로 버튼을 생성해보자 얍!")

# 버튼들을 담은 리스트 생성
buttons = []

# 반복문으로 버튼을 생성
for i in range(1, 6):
    if i == 2:
        button_text = f"버튼 {i}번 노랑"
        button_bg   = "yellow"
    elif i == 3:
        button_text = f"버튼 {i}번 녹색"
        button_bg   = "green"
    elif i == 5:
        button_text = f"버튼 {i}번 주황"
        button_bg   = "orange"
    else:
        button_text = f"버튼 {i}번 보통"
        button_bg   = "lightgray"
    button = Button(window, text=button_text, bg=button_bg, command=lambda x=i: button_click(x))
    button.pack()
    buttons.append(button)
    
window.mainloop()