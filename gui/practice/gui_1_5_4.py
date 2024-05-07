from tkinter import *

def button_click(idx):
    if idx % 2 == 1:
        buttons[idx-1]["bg"] = "green"
        print(f"버튼 {idx}번을 클릭했고 해당 버튼이 녹색으로 변경되었습니다")
    else:
        print(f"버튼 {idx}번을 클릭했습니다")
    
window = Tk()
window.title("반복문으로 버튼 생성하기")

buttons = []

for i in range(1, 6):
    if i == 2:
        button_text = f"버튼 {i}번"
        button_bg   = "yellow"
    else:
        button_text = f"버튼 {i}번"
        button_bg   = "lightgray"
    button = Button(window, text=button_text, bg=button_bg, command=lambda idx=i: button_click(idx))
    button.pack()
    buttons.append(button)
    
window.mainloop()