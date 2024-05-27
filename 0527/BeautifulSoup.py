# [웹 스크래핑] 웹 스크래핑의 개념과 정적 웹 스크래핑
# https://velog.io/@ehddnr7355/%EC%9B%B9-%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91%EC%9D%98-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%8B%A4

import requests
from bs4 import BeautifulSoup

# www.example.com 사이트를 요청한 후 응답 받기
res = requests.get("https://www.example.com")

# BeautifulSoup 객체를 생성
# 첫번째 인자로는 response의 body를 텍스트로 전달
# 두번째 인자로는 "html"로 분석한다는 것을 명시
soup = BeautifulSoup(res.text, "html.parser")

# 객체 soup의 .prettify()를 활용하면 분석된 HTML을 보기 편하게 반환
print(soup.prettify())

# soup 객체를 통해서 HTML의 특정 요소를 가지고 올 수 있음
print(soup.title)
print(soup.head)
print(soup.body)

# <h1> 태그로 감싸진 요소 하나 찾기
h1 = soup.find("h1")
# <h1> 태그로 감싸진 요소들 찾기
h1_ = soup.find_all("h1")

print(h1.name) # 태그 이름 가져오기
print(h1.text) # 태그 내용 가져오기