def solution(shirt_size):
    sizes = {"XS": 0, "S": 0, "M": 0, "L": 0, "XL": 0, "XXL": 0}
    for size in sizes:
        sizes[size] = shirt_size.count(size)
    return sizes
    
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
print(solution(shirt_size))