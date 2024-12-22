import tkinter as tk
from functools import partial

def add_numbers(num1, num2):
    
    result = int(num1) + int(num2)
    result_label.config(text=f"Result: {result}")
    
    
root = tk.Tk()
root.title("계산기")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

add_button = tk.Button(
    root,
    text="추가",
    command=partial(add_numbers, entry1.get, entry2.get)
)
add_button.pack(pady=10)

result_label = tk.Label(root, text="결과: ")
result_label.pack(pady=10)

root.mainloop()