from tkinter import *
def update_label(ipt, opt):
    opt.config(text=ipt.get())
def button_event():
    name_update_label()
    number_update_label()
def name_update_label():
    update_label(input_name, output_name)
def number_update_label():
    update_label(input_number, output_number)

# 윈도우    
window = Tk()
window.title("GUI 테스트")
window.geometry("500x400")

# 이름 입출력
input_name = Entry(window)
output_name = Label(window)

# 숫자 입출력
input_number = Entry(window)
output_number = Label(window)

# 버튼
confirm = Button(window, text="확인", command=button_event)

# 레이아웃
input_name.pack()
input_number.pack()
output_name.pack()
output_number.pack()
confirm.pack()

window.mainloop()