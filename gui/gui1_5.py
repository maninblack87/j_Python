from tkinter import *

# 임시 함수명 processing
def processing(input, output):
    output.config(text=input.get())

# 배열
arr = []

# GUI
window = Tk()
window.title("GUI 테스트~~")
window.geometry("500x400")

ipt0 = Entry(window)
ipt1 = Entry(window)
ipt2 = Entry(window)
ipt3 = Entry(window)
ipt4 = Entry(window)
ipt5 = Entry(window)
ipt6 = Entry(window)
ipt7 = Entry(window)
btn = Button(window, text="실행", command=lambda:processing)

ipt0.pack()
ipt1.pack()
ipt2.pack()
ipt3.pack()
ipt4.pack()
ipt5.pack()
ipt6.pack()
ipt7.pack()
btn.pack()

window.mainloop()