import tkinter as tk

def add_numbers():
    
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    result = num1 + num2
    
    result_label.config(text=f"Result: {result}")
    

root = tk.Tk()
root.title("계산기")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

add_button = tk.Button(root, text="추가", command=add_numbers)
add_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()