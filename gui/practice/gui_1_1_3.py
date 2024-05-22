from tkinter import *

# 함수 : 레이블에 입력값을 표시
def update_label(i, o):
    o.config(text=i.get())
# 함수 : opt_name(이름 출력)
def confirm_update_label():
    update_label(ipt, opt)

window = Tk()
window.title("GUI")

opt = Label(window)
ipt = Entry(window)
confirm = Button(window, text="클릭", command=confirm_update_label)

ipt.pack()
opt.pack()
confirm.pack()

window.mainloop()