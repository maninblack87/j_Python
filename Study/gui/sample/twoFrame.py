import tkinter as tk

root = tk.Tk()
root.title("서로 다른 레이아웃을 가진 두 개의 Frame 예제")

# 첫 번째 Frame에 pack() 배치 매니저 사용
frame1 = tk.Frame(root, width=200, height=200, bg="lightblue")
frame1.pack(padx=10, pady=10)

label1 = tk.Label(frame1, text="첫 번째 Frame - pack()")
label1.pack(side='left', padx=10, pady=10)

label1 = tk.Label(frame1, text="첫 번째 Frame - pack()")
label1.pack(side='left', padx=10, pady=10)

# 두 번째 Frame에도 pack() 배치 매니저 사용
frame2 = tk.Frame(root, width=200, height=200, bg="lightgreen")
frame2.pack(padx=10, pady=10)

label2 = tk.Label(frame2, text="두 번째 Frame - pack()")
label2.pack(padx=10, pady=10)

root.mainloop()
