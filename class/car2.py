class Car:
    
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year
        
    def description(self):
        return f"{self.make} {self.year} {self.model}"
        
    def start_engine(self):
        return f"{self.make} {self.year} {self.model}의 엔진이 가동되고 있습니다"