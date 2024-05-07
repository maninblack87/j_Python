from tkinter import *

# 버튼을 클릭하면 이벤트 발생
def button_click(button_id):
    print(f"버튼 {button_id}가 클릭되었습니다")
    
# tkinter 윈도우 생성
window = Tk()
window.title("반복문으로 생성된 버튼 속성 수정하기")

# 버튼을 생성하고 배치하는 반복문
buttons = []
for i in range(1, 6):
    if i == 2:
        button_text = "다른 텍스트"
        button_bg = "yellow"
    else:
        button_text = "버튼" + str(i)
        button_bg = "lightgray"
    button = Button(window, text=button_text, bg=button_bg, command=lambda x=i: button_click(x))
    button.pack()
    buttons.append(button)  # 생성된 버튼을 리스트에 추가
    
# 두번째 버튼의 속성 수정
buttons[3]["text"] = "수정된 텍스트"
buttons[3]["bg"] = "green"

window.mainloop()