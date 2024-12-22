from tkinter import *

def button_click(buttons, idx):
    current_bg = buttons[idx]["bg"]
    if current_bg == "lightgray":
        buttons[idx]["bg"] = "green"
        print(f"버튼 {idx}번을 클릭했고 해당 버튼이 녹색으로 변경되었습니다")
    elif current_bg == "green":
        buttons[idx]["bg"] = "red"
        print(f"버튼 {idx}번을 클릭했고 해당 버튼이 빨강색으로 변경되었습니다")
    elif current_bg == "red":
        buttons[idx]["bg"] = "blue"
        print(f"버튼 {idx}번을 클릭했고 해당 버튼이 파랑색으로 변경되었습니다")
    elif current_bg == "blue":
        buttons[idx]["bg"] = "lightgray"
        print(f"버튼 {idx}번을 클릭했고 해당 버튼이 파랑색으로 변경되었습니다")
        

window = Tk()
window.title("반복문으로 버튼 생성하기")

buttons = []

for i in range(0, 5):
    button_text = f"버튼 {i+1}"
    button_bg   = "lightgray"
    button = Button(window, text=button_text, bg=button_bg, command=lambda idx=i: button_click(buttons, idx))
    button.pack()
    buttons.append(button)

window.mainloop()