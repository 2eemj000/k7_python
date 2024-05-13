# 구글 검색, chatGPT 사용하여 다음 코드를 완성 

import random

# 빈 리스트 생성
random_numbers = []

# 난수를 20개 생성하여 리스트에 추가
for _ in range(20):
    random_numbers.append(random.randint(1, 100))

# 저장된 리스트 출력
print(f"난수 생성 = {random_numbers}")
print('')
# s 다음에 숫자를 가진 변수들을 생성하여 리스트에 저장하는 예제

# 빈 리스트 생성
string_list = []

# s 다음에 숫자를 가진 변수들 생성하여 리스트에 추가: s1, s2, s3 등을 생성 
for i in range(1, 21):
    s_number= f"s{i}"
    string_list.append(s_number)
   
# 저장된 리스트 출력
print(f"sno 리스트 = {string_list}")
print('')

students = string_list
scores = random_numbers

# students, scores로 구성된 딕셔너리를 만든다 
# zip() : 두 개 이상의 리스트를 동시에 반복하면서 요소들을 묶어줌
# students를 key로, scores를 value로
score_dic = dict(zip(students, scores))


print(f"학번과 점수 딕셔너리={score_dic}")
print('')
# 점수를 기준으로 내림차순으로 정렬한 튜플 리스트 생성
# sorted() : 딕셔너리를 정렬, 튜플리스트로 반환
# 기본적으로는 딕셔너리의 키를 기준으로 정렬하지만, key 매개변수를 이용하여 값을 기준으로 정렬가능
# reverse=True : 내림차순
sorted_scores = sorted(score_dic.items(), key=lambda x: x[1], reverse=True)

# 정렬된 튜플 리스트를 다른 딕셔너리에 저장
# (sorted_score_dic에는 점수를 기준으로 내림차순으로 정렬된 새로운 딕셔너리가 저장)
# a[0]번째의 sorted_score_dic값에 a[1]값 대입
sorted_score_dic = {}
for a in sorted_scores:
    sorted_score_dic[a[0]]=a[1]

# 결과 출력
print(f"점수로 정렬된 딕셔너리= {sorted_score_dic}")
print('')
# 정렬된 튜플 리스트에서 상위 5개 추출하여 리스트로 저장
# 상위 5개 추출하여 딕셔너리로 저장
top_5 = sorted_scores[:5]

# 결과 출력
print(f"상위 5개= {top_5}")
print('')
# 딕셔너리의 키-값 쌍을 튜플로 묶어 리스트에 추가
score_list = list(sorted_score_dic.items())

# 결과 출력
print(f"리스트로 변환된 딕셔너리: {score_list}")
print('')

# 딕셔너리의 각 요소를 enumerate를 사용하여 변환
# enumerate() 함수 : 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
# enumerate(sorted_score_dic.items(), 1)에서 1은 시작하는 값
transformed_score_dic = {}
for index, (key, value) in enumerate(sorted_score_dic.items(), 1):
    transformed_score_dic[f"student_{index}"] = (key, value)

# 결과 출력
print(f"변환된 딕셔너리: {transformed_score_dic}")
print('')