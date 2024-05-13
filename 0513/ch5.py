a=5
if a <100:
    print('right!')

# score=int(input())
# if (90<=score) and (score<=100):
#     print('A')
# elif (80<=score) and (score<90):
#     print('B')
# else:
#     print('F')

# if만 있으면 논리적오류
# else:
    #TODO 적어두면 빠뜨리지 않을 수 있음

msg='hello'
if msg == 'hello':
    print("right!")

data=[1,2,3]
if data==[1,2,3]:
    print("right!")

# if []:
#     print("right!!!") -> 공백일때는 실행 X

data=[1,2,3]
if 2 in data:
    print('Here!')

string = 'hello'
if 'e' in string:
    print("Here!!!")

a=5
print(a<100)

string = 'hello'
print(string.capitalize())
if 'H'in string:
    print("Here!!")
if 'h'in string:
    print("!!Here!!")

string = 'Hello'
if 'h'in string.lower():
    print("!!Here!!")

a=3
if a<5 or a>10:
    print('a')

print(sum([True,True, False]))
# 너무 많은 데이터 분석해야할때 쓰일 수 있음

data=[1,2,3,4]
for a in data:
    if a<3:
        print(a)
    else:
        print('wrong!')
