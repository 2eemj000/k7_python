pizza = ['a','b','c']
for d in pizza:
    print(d, end=" ")
    print(f"나는 {d}피자가 좋습니다")
print("나는 정말 피자를 사랑합니다")

animal = ['강아지', '고양이', '곰']
for d in animal:
    print(f"{d}는 훌륭한 반려동물입니다")

number=range(1,21)
for a in number:
    print(a, end=" ")

number2=list(range(1,1000001))
# for a in number2:
    # print(a, end=" ")
print()
print(min(number2))
print(max(number2))
print(sum(number2))

number3=range(1,21,2)
for a in number3:
    print(a, end=" ")
print()

number4=range(3,31,3)
for a in number4:
    print(a, end=" ")
print()

for a in range(1,11):
   print(a**3, end=" ")
print()

print([i**3 for i in range(1,11)])
# print(i**3 for i in range(1,11)) -> X (리스트 내포 문법으로 써야함)

pizza = ['a','b','c','d','e']
for d in pizza:
    print(d, end=" ")
    print(f"나는 {d}피자가 좋습니다")
print("나는 정말 피자를 사랑합니다")
print(f"리스트의 첫 두 항목은 {pizza[:2]}입니다")
print(f"리스트의 중간 세 항목은 {pizza[1:4]}입니다")

friend_pizza=pizza[:]
friend_pizza[1]='f'
print(friend_pizza)