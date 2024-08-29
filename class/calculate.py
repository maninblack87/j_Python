class Calculator:
    
    def __init__(self, num1, num2, result_label):
        self.num1 = num1
        self.num2 = num2
        self.result_label = result_label
    
    def sum_numbers(self):
        self.result = int(self.num1) + int(self.num2)
        self.result_label.config(text=f"Result: {self.result}")
        
    def sub_numbers(self):
        self.result = int(self.num1) - int(self.num2)
        self.result_label.config(text=f"Result: {self.result}")
        
    def mul_numbers(self):
        self.result = int(self.num1) * int(self.num2)
        self.result_label.config(text=f"Result: {self.result}")
        
    def div_numbers(self):
        self.result = int(self.num1) / int(self.num2)
        self.result_label.config(text=f"Result: {self.result}")