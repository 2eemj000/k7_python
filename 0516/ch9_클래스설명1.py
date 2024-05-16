# https://codermun-log.tistory.com/73

class Dog2:
    """클래스 Dog 정의""" 

    # __init__ : Dog클래스를 기반으로 인스턴스를 만들 때마다 파이썬이 자동으로 실행하는 특별메서드
    # __ : 파이썬에서 자동호출을 의미
    # initialize (초기화) / ()안에는 parameter로 전달 
    # self : 생성된 객체를 의미, 맨앞에 위치하는 필수 매개변수, 
    def __init__(self, name, age, address): # 속성을 정의한다는 뜻
        """클래스 Dog의 생성자"""
        # 데이터 멤버 선언 (name, age, city), self가 이 세개를 가리킴
        # self.속성 = 값
        self.name = name
        self.age = age
        self.city = 'busan' # city는 고정적으로 busan
        self.__address = address # 변수앞에 __를 붙여 비공개속성으로 만듦(클래스 밖에서 접근X)

    def sit(self):
        print(f"{self.name}개가 앉기")
    
    def __greeting(self): # 함수도 비공개로 선언하면 클래스 밖에서 접근X
        print('Hello')

myDog = Dog2("hong", 10) # 인스턴스생성(생성자호출,객체생성), 이때 자동으로 self를 통해 접근하게됨
myDog.sit() # 함수호출, ()안에 비워둠