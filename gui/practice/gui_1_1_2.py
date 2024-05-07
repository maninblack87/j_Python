from tkinter import *

def update_label(input, output):
    output.config(text=input.get())
    
def confirm_update_label():
    update_label(ipt_name, opt_name)

window = Tk()
window.title("GUI 테스트")
window.geometry("500x400")

ipt_name = Entry(window)
opt_name = Label(window)
confirm  = Button(window, text="확인")

ipt_name.pack()
opt_name.pack()
confirm.pack()

window.mainloop()