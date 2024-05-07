from tkinter import *

# 버튼을 클릭하면 이벤트가 발생하는 함수
def button_click(button_id):
    print(f"버튼 {button_id}가 클릭 되었습니다.")
    
# tkinter 윈도우 생성
window = Tk()
window.title("반복문으로 생성된 버튼 속성 수정하기")

# 버튼을 생.성.하고 배.치.하는 반복문
buttons = []
for i in range(1, 6):
    # 변수를 통해 버튼 속.성.을 설정한다
    # 버튼 2는 노란색으로 "노란 버튼" 텍스트로
    if i == 2:
        button_text = "노란 버튼"
        button_bg   = "yellow"
    # 나머지는 노멀하게
    else:
        button_text = "버튼" + str(i)
        button_bg   = "lightgray"
    button = Button(window, text=button, bg=button_bg, command=lambda idx=i: button_click(idx))
    button.pack()           # 실제로 윈도우에 생성되는 부분
    buttons.append(button)  # 이건 buttons라는 리스트에 추가하는 것 뿐이다

button[3]["text"] = "수정된 텍스트"
button[3]["bg"] = "green"
    
window.mainloop()