import tkinter as tk

def add_numbers():
    
    try:
        # 입력된 값 가져오기
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # 두 숫자의 합 계산
        result = num1 + num2
        
        # 결과를 레이블에 표시
        result_label.config(text=f"Result: {result}")
        
    except ValueError:
        
        # 잘못된 입력 처리 
        result_label.config(text="Please enter valid numbers")
        
# GUI 애플리케이션 생성
root = tk.Tk()
root.title("Simple Calculator")

# 첫 번째 숫자 입력 필드
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# 두 번째 숫자 입력 필드
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# "Add" 버튼
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)

# 결과를 표시할 레이블
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# GUI 애플리케이션 실행
root.mainloop()