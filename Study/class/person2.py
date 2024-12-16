class Person2:
    
    # 생성자 메서드
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    # 나이 출력 메서드
    def greet(self):
        print(f"안녕하세요 이름은 {self.name}, 나이는 {self.age}")
    
    # 생일 처리 메서드
    def have_birthday(self):
        self.age += 1
        print(f"{self.name}이(가) {self.age}번째 생일을 보냈습니다")