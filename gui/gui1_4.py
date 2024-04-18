from tkinter import *

def update_label(input, output):
    output.config(text=input.get())
    
window = Tk()
window.title("GUI테스트")
window.geometry("500x400")

input_myname = Entry(window)
output_myname = Label(window)
button_myname = Button(window, text="확인", command=lambda:update_label(input_myname, output_myname))

input_myname.pack()
output_myname.pack()
button_myname.pack()

window.mainloop()