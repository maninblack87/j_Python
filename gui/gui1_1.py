from tkinter import *

def update_label(input, output):
    output.config(text = input.get())
    
def confirm_update_label():
    update_label(input_myname, output_myname)
    
window = Tk()
window.title("GUI 테스트")
window.geometry("500x400")

input_myname = Entry(window)
output_myname = Label(window)
confirm_myname = Button(window, text="확인", command=confirm_update_label(input_myname, output_myname))

input_myname.pack()
output_myname.pack()
confirm_myname.pack()

window.mainloop()