from tkinter import *

# 메서드 : 레이블에 입출력
def update_label(input, output):
    output.config(text=input.get())
# 메서드 : 이름 갱신
def confirm_update_label():
    update_label(ipt_name, opt_name)

window = Tk()
window.title("GUI 테스트")
window.geometry("500x400")

ipt_name = Entry(window)
opt_name = Label(window)
confirm = Button(window, text="확인", command=confirm_update_label)

ipt_name.pack()
opt_name.pack()
confirm.pack()

window.mainloop()