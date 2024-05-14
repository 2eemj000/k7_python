# PART 1
def ten_times(func):
    for i in range(5):
        func()
def print_hello():
    print("hello")
ten_times(print_hello) # 함수를 parameter로 전달할 수 있음



# PART 2
def add(x,y):
    return x+y
def apply_operation(operation, x,y):
    return operation(x,y)
result = apply_operation(add,3,4) # 함수와 변수를 parameter로 한꺼번에 전달



# PART 3 - map & list
def power(item):
    return item**2
def under_three(item):
    return item<3
lst=[1,2,3,4,5]
map_list=map(power,lst)
print(list(map_list))
filter_list=filter(under_three,lst)
print(list(filter_list))



# PART 4 - 람다식
m_list =list(map(lambda x:x*x,lst))
print(m_list)
