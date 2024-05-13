# data=[1,2,3,3,3]
# print(data, type(data))

# # data=list()
# # print(data,type(data))

# print(data[0])
# print(data[1])
# print(data[2])

# # print(data[3])

# data.append(6)
# data.append(7)
# data.append(8)
# data.append(9)
# data.append(10)
# print(len(data))

# data[3]=4
# data[4]=5
# del data[1]
# print(data,len(data),sum(data),min(data),max(data))

# data=list(range(1,11))
# print(data,type(data))

# data=list(range(10,0,-1))
# print(data,type(data),sorted(data))

# data = input()
# data = data.split() #list
# data = list(map(int, data))

# # data = input()
# # data = data.split() #list
# # data = list(map(int, data))

# # 위 세줄이랑 같은 의미 한줄로
# data = list(map(int, input().split()))
# data=[1,2,3,4,5]
# print(data,type(data),type(data[0]))
# print(sum(data))

# data=[1,2,3.14, 'hello', len, range(5)]
# for d in data:
#     print(d,type(d))

# data=[1,2,3,4,5]
# print(data[len(data)-1])
# # ::-1 range 반대로 나열해줌
# print(data[::-1])

# msg='aga'
# print(msg==msg[::-1]) 
# msg.reverse() 위랑 같은 의미 (역순으로 바꾼다)

data=[5,3,4,2,1]
print(data[len(data)-1])
print(data[::-1])

data.append(1)
print(data)
data.pop()
print(data)

data.insert(1,222)
print(data)

del data[1]
print(data)

data.remove(1)
print(data)

print(sorted(data)) # sorted는 data를 바꾸지 않음
print(data)

data.sort() # data 자체를 변경시켜버림
print(data)

sorted_data=sorted(data) # 실제로는 이런식으로 코드를 짜는게 좋음 (변수로 확실히 구분하도록)
print(sorted_data)