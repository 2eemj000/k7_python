car='subaru'
print("Is car == 'subaru'? I predict True.")
print(car=='subaru')

print("\nIs car == 'audi'? I predict False")
print(car=='audi')

name = 'Lee Minju'
print('minju' in name)
print('minju' in name.lower())

alien_color = 'green'
if alien_color=='yellow':
    print("플레이어가 5점을 획득했습니다 !")

alien_color = 'yellow'
if alien_color=='yellow':
    print("플레이어가 5점을 획득했습니다 !")
else:
    print("플레이어가 10점을 획득했습니다 !")

alien_color = 'green'
if alien_color=='yellow':
    print("플레이어가 5점을 획득했습니다 !")
elif alien_color=='red':
    print("플레이어가 10점을 획득했습니다 !")
else:
    print("플레이어가 15점을 획득했습니다 !")

age=int(input())
if age<2:
    print("영아입니다")
elif (age<4 and age>=2):
    print("유아입니다")
elif (age<13 and age>=4):
    print("어린이입니다")
elif (age<20 and age>=13):
    print("십대입니다")
elif (age<65 and age>=20):
    print("성인입니다")
else:
    print("노인입니다")

favorite_fruits=['사과','배','바나나','수박']
if '바나나' in favorite_fruits:
    print("바나나를 좋아하는군요")

user=['가영','나영','다영','admin']
for a in user:
    if a=='admin':
        print("관리자님 안녕하세요. 상태 보고서를 보시겠습니까?")
    else:
        print(f"{a}님 안녕하세요. 다시 로그인해 주셔서 감사합니다 !")


if user:
    for a in user:
        print (f"Adding {a}")
    print("\nFinished adding!")
else:
    print("사용자가 있어야 합니다")

hello_admin = []
if hello_admin:
    for a in hello_admin:
        print (f"Adding {a}")
    print("\nFinished adding!")
else:
    print("사용자가 있어야 합니다")

user_ids = ["Lee", "park", "KIM"]
new_ids = ["lee", "choi", "Son"]
