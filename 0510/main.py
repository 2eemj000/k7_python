# https://docs.python.org/3/library/stdtypes.html
# https://www.w3schools.com/python/ref_string_find.asp

print('hello, world!')

age=5
pi=3.14
c='hello, world!'
d=[1,2,3]
e='everything' or 'object'
print(type(age),type(pi),type(c),type(d),type(e))

def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b) 
    print(a**b)
a=5
b=9

# a=3.14
# b=1.2
# calc(a,b)

# a=3.14
# b=1_000_000_000
# print(a,b)
# calc(a,b)

# #swap
# temp=a
# a=b
# b=temp
# print(a,b)

# # a,b=map(int, input().split())
# b, a=a, b
# print(a,b)

msg = 'hello, world!'
print(msg, type(msg))

print(msg.title())
print(msg.capitalize())
print(msg.find('l'))
print(msg[0])
print(msg[1])
# msg[0]='H'
# print(msg) -> error (string은 한번 할당되면 바꿀 수 없음)

# f-문자열
a='hello'
b='world'
def add(a,b):
    return a+b
print(f'{a},{b}, {add(1,2)}! hahahaha!')

# 수정