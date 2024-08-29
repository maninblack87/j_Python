class Person:
    
    # 생성자 메서드
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    # 나이 출력 메서드
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    # 나이를 한 살 더하는 메서드
    def hava_birthday(self):
        self.age += 1