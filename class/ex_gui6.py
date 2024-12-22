import tkinter as tk
from functools import partial
from calculate import Calculator

root = tk.Tk()
root.title("계산기")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

cal = Calculator(entry1.get(), entry2.get())

sum_button = tk.Button(
    root,
    text="추가",
    command=partial(Calculator.sum_numbers, entry1.get,)
)