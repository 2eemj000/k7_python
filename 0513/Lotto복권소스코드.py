#100장 복권 발행 후 list에 저장 -> 정렬 -> for문으로 하나씩 꺼내서 당첨여부확인

#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random

# 두 세트 생성
set1 = {1, 2, 3, 4, 5}
set2 = {3, 2, 1, 6, 7}

# 두 세트가 동일한지 확인 (모든 요소가 같은지)
print("set1과 set2가 동일한지:", set1 == set2)
print(len(set1.intersection(set2))==3) # intersection : 교집합

# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    # random이라는 class의 sample함수
    # numbers 리스트에서 6개를 랜덤으로 골라 set만듦
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number # 함수정의에 return type을 안 정하니까 => 한꺼번에 여러개를 return할 수 있음 (각각)

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers() # 마찬가지로 여러 변수에 한꺼번에 함수적용 가능
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number) 

# 100장의 로또 번호 생성하여 당첨 여부 판별
for idx in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    
    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인 (set비교)
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 1등 당첨!")
    elif lotto_numbers == winning_numbers:
        print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    elif lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 5: # 교집합의 길이가 5니까 5개의 숫자가 일치하는걸 의미
        print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 4:
        print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
    else:
        print(f"{idx}번째 로또 복권: 꽝")