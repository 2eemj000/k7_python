data=[1,2,3]
for d in data:
    print(d, end=" ")
print('-', data[1])

string='hello'
for s in string:
    print(s, end=" ")
print('-', string[1])
# string[1] = 'F'
# print('-', string[1]) -> string은 변경불가
data = (1,2,3)
for i in data:
    print(i)
# data[1]=5 -> 튜플()도 마찬가지

data2 = [i**2 for i in data]
print(data2, type(data2))
# data3랑 같은 의미인데 짧게 쓸 수 있음

data3 = []
for i in data:
    data3.append(i**2)
print(data3)

data4 = [i**2 for i in data if i**2<5]
print(data4, type(data4))
# data5랑 같은 의미인데 짧게 쓸 수 있음

data5 = []
for i in data:
    if i**2 < 5:
        data5.append(i**2)
print(data5)
# 탭넣는것 중요

# for (int i=0;i<10;i++)

data=[]
for d in data:
    print(d)

for _ in range(10):
    print('a', end=" ")
# for 뒤에 비워두려면 _

for idx, d in enumerate(data):
    print(idx,d)
# enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌

# for문 중첩 -> 탭넣는것 중요
data_1r = range(1,10)
data_2r = range(1,10)
for a in data_2r:
    for b in data_1r:
        print(f'{a}*{b}={a*b}')
    print()

# data = range(1,1001) -> X (list써야함)
# print(data, type(data))
# range(1, 1001) <class 'range'> 이렇게 나옴

data = list(range(1,1001,2))
print(data, type(data))

# [1,11)
data=list(range(1,11))
# [1,5)
print(data[1:5])
print(data[-1])
print(data[0:-1])
# 데이터를 반으로 나눌때 자주 쓰임
print(data[:5], data[5:], sep="\n")
# reverse
print(data[::-1])
print(sorted(data, reverse=True))

def swap(a,b):
    temp=a
    a=b
    b=temp
    # a,b=b,a로 바로 바꿀 수 있음

# a,b=1,2
# print(a,b)
# swap(a,b)
# print(a,b)
# -> 결과 바뀌지 않음

data = [1,2,3]
# data2=data.copy() 도 아래랑 같은 의미
data2=data[:] 
# data2는 data를 리스트 복사해서 써야함, 아니면 data자체가 바뀜
data2[1]=5
print(data, data2, sep="\n")

# 튜플로 바꿔서 에러찾으면 더 편할 수 있음 (?)
data = (1,2,3)
data2=data
# data2는 data를 리스트 복사해서 써야함, 아니면 data자체가 바뀜
data2[1]=5
print(data, data2, sep="\n")

