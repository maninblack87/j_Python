import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html;charset=utf-8'
    }

# 1. 입력한 레벨의 제목을 추출하는 메소드
def title_of_backrooms():
    
    ipt = int(input("알고싶은 백룸의 레벨을 입력해주세요: "))
    
    url = f"https://backrooms.fandom.com/wiki/Level_{ipt}"
    
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    firstHeading = soup.find(id = "firstHeading").text.strip()
    
    print(firstHeading)
    
# 테스트1
# print(title_of_backrooms())

# 2. 입력한 범위의 여러(!) 레벨의 제목을 추출하는 메소드
def many_titile_of_backrooms():
    
    first = int(input("알고싶은 백룸의 레벨을 입력해주세요(시작점): "))
    last = int(input("알고싶은 백룸의 레벨을 입력해주세요(종료점): "))
    # >> 예외처리
    if first > last:    # 스왑
        tmp = first
        first = last
        last = tmp
    
    for i in range(first, last+1):
        
        url = f"https://backrooms.fandom.com/wiki/level_{i}"
        
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        firstHeading = soup.find(id = "firstHeading").text.strip()
        
        print(firstHeading)
        
# 테스트2
print(many_titile_of_backrooms())