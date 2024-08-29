class ShirtSize:
    
    def __init__(self, shirt_size):
        self.sizes = {"XS": 0, "S": 0, "M": 0, "L": 0, "XL": 0, "XXL": 0}
        for size in self.sizes:
            self.sizes[size] = shirt_size.count(size)
            
    def display_size_info(self):
        for size in self.sizes:
            print(size + "의 수량:" + str(self.sizes[size]))
        
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
case_a = ShirtSize(shirt_size)
case_a.display_size_info()