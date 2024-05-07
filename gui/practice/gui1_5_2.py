from tkinter import *

def button_event(idx):
    print(f"버튼 {idx}을(를) 클릭했다")
    
window = Tk()
window.title("반복문으로 상호작용하는 버튼 만들기")

# 버튼들의 리스트를 생성한다
buttons = []

for i in range(5):
    if i == 1:
        button_bg = "yellow"
    elif i == 2:
        button_bg = "green"
    else:
        button_text = f"버튼 {i+1}번"
        button_bg   = "lightgray"
    button = Button(window, text=button_text, bg=button_bg, command=lambda x=i: button_event(x))
    button.pack()
    buttons.append(button)
    
window.mainloop()