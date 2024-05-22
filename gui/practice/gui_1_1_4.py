from tkinter import *
def update_label(ipt, opt):
    opt.config(text=ipt.get())
def name_update_label():
    update_label(input_name, output_name)
def favorite_number_update_label():
    update_label(input_number, output_number)
def button_confirm_event():
    name_update_label()
    favorite_number_update_label()
    
window = Tk()
window.title("엔트리에 입력하면 레이블에 출력시키기")
window.geometry("500x400")
# 이름을 입출력한다
input_name = Entry(window)
output_name = Label(window)
input_name.pack()
output_name.pack()
# 좋아하는 숫자를 입출력한다
input_number = Entry(window)
output_number = Label(window)
input_number.pack()
output_number.pack()
# 버튼
confirm = Button(window, text="확인", command=button_confirm_event)
confirm.pack()
window.mainloop()