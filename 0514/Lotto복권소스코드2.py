#100장 복권 발행 후 list에 저장 -> 정렬 -> for문으로 하나씩 꺼내서 당첨여부확인 + 당첨확인 함수로 구현

import random

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

def check_winner(lotto_numbers, lotto_bonus_number,winning_numbers,winning_bonus_number, idx):
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

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers() # 마찬가지로 여러 변수에 한꺼번에 함수적용 가능
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number) 
lotto_list=[] # 로또넘버, 보너스넘버 append시키기

# 100장의 로또 번호 생성하여 당첨 여부 판별
for idx in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers() # 복권 한장 만드는걸 100번 반복
    lotto_list.append((idx, lotto_numbers, lotto_bonus_number))
    # enumerate를 사용하여 딕셔너리의 각 요소를 (인덱스, 값) 튜플 형태로 변환 (복권번호, 보너스번호) 튜플로 저장 
    # 100장 복권을 저장 (딕셔너리의 키-값 쌍을 튜플로 묶어서 리스트에 추가)

for idx, lotto_numbers, lotto_bonus_number in lotto_list:
    # 100장 복권을 가져와 당첨번호와 비교
    check_winner(lotto_numbers, lotto_bonus_number,winning_numbers,winning_bonus_number, idx)