# https://blockdmask.tistory.com/520

# 일반함수
# def is_even(x):  
#       return x % 2 == 0
# 람다로 표현
# is_even = lambda x : x % 2 == 0

# is_even(1) # False
# is_even(2) # True

is_even = lambda x : x % 2 == 0
print(is_even(1)) 



# map(함수, 리스트나 튜플) : 함수를 리스트나 튜플 각각의 element에 돌아가면서 적용

# 1. 일반 함수 버전
def plus_two(x):
    return x + 2

result1 = list(map(plus_two, [1, 2, 3, 4, 5]))
print(result1)

# 2.  람다 함수 버전
result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))
print(result2)



# filter(함수, 리스트나 튜플) : map + boolean(T/F)

# 1. 일반 함수 버전
def is_even(x):
    return x % 2 == 0

result1 = list(filter(is_even, range(10)))  # [0 ~ 9]
print(result1)

# 2.  람다 함수 버전
result2 = list(filter((lambda x: x % 2 == 0), range(10)))  # [0 ~ 9]
print(result2)
