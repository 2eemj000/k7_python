from random import randint
from random import choice
print(randint(1,6))
players = ['a','b','c','d','e','f']
print(choice(players))


# class 변수
class Student:
    count = 0 # count는 클래스변수
    def __init__(self):
        Student.count+=1 # 클래스변수값 변경

# 클래스 메서드 사용 (@classmethod 써서)
    @classmethod
    def printing(self):
        print(f"클래스 메서드 출력 = {Student.count}")

print(f"{Student.count}") # 클래스변수 접근
s=Student()
print(f"{Student.count}")
Student.printing() # 클래스 메서드의 호출 (객체없이)

def initialize():
    return 1,2,3

_,a,b = initialize() # 세개를 받을건데 하나는 안쓸거라면 _표시

a=[1,2,3]
b=[4,5,6]
mergeList = [*a,*b] # 리스트에 *쓰면 iterable객체를 나타내고 unpacking 하는 역할
print(mergeList)

# class instance에 대한 인덱싱과 슬라이싱 처리
class MyList:
    def __init__(self, data):
        self.data = data
    def __getitem__(self,index): # !자주 사용됨!
        return self.data[index]
    
mlist = MyList([1,2,3,4])
print(mlist[1:3]) # __getitem__ : 객체인 mlist에 슬라이싱한걸 넣으면 자동으로 list가 됨
s=['s1','s2','s3']
num=[5,3,7]
# zip() 함수 : 여러 개의 순회가능한 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자를 반환
score = zip(s,num)
for a,b in score: # zip을 다시 []로 묶어줌
    print(f"[{a},{b}]")