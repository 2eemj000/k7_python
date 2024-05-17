# score = int(input())
# if score >= 0 and score <= 100:
#     print("입력한 점수:", score)
#     if score >= 90 and score <= 100:
#         print ("A")
#     elif score >= 80 and score <= 89:
#         print ("B")
#     elif score >= 70 and score <= 79:
#         print ("C")
#     elif score >= 60 and score <= 69:
#         print ("D")
#     else:
#         print ("F")
# else:
#     print("0부터 100까지의 범위 내에서 입력하세요.")

# year=int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(1)
# else:
#     print(0)

# time = input().split(' ')
# H = int(time[0])
# M = int(time[1])
# if M >= 45:
#     print(H, (M - 45))
# else:
#     if H == 0:
#         print(23, M + 15)
#     else:
#         print(H - 1, M + 15)

# n = int(input())
# print(sum(i for i in range(1, n+1)))

# N=int(input())
# for i in range(1, N+1):
#     print(" "*(N-i) + "*"*i)

# N=int(input())
# n_list = list(map(int, input().split()))
# v=int(input())
# print(n_list.count(v))

# N, X = map(int, input().split())
# A=list(map(int, input().split()))
# # 파이썬에서는 for 루프나 range() 함수를 사용하여 반복을 수행할 때 C나 Java와 같은 다른 언어와는 다르게 for 루프 내에서 인덱스 값을 직접 조작하는 방식은 지원되지 않습니다.
# # if A[int i=0;i<N;i++] < X:
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")

# N=int(input())
# n_list = list(map(int, input().split()))
# # list() 함수는 하나의 인자만을 받을 수 있음
# # end 매개변수는 print() 함수에서 사용되는 것이기 때문에 list() 함수에 사용할 수 없음
# # min_max = list(min(n_list),max(n_list),end=" ")
# print(min(n_list), max(n_list),  end=" ")

# # N은 바구니갯수, M은 공을 넣는 총 회차
# # i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣음
# # list는 변경가능한 mutable
# N,M=map(int, input().split())
# arr = [0]*(N+1)
# # a++라는 표현식은 파이썬에서 X, 대신에 a += 1과 같은 방식으로 사용
#     # for (int a=1;a<M+1,a++):
#     #     if (a>=i)&(a<=j):
#     #         arr[a-1]=k
# # 리스트 슬라이싱은 리스트의 일부분을 복사하여 반환하는 것이므로 단일 값을 할당하는데 사용X
# # 대신에 각 인덱스를 반복하여 값을 할당해야함
#     # for k in range(1, M+1):
#     #     i,j=map(int, input().split())
#     #     arr[range(i,j+1,1)] = k
#     # print(arr)
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for n in range(i, j+1):
#         arr[n] = k
# for i in range(1,N+1):
#     print(arr[i], end=' ')

# N,M=map(int, input().split())
# list=[i for i in range(1,N+1)]
# for i in range(M):
#     i, j = map(int, input().split())
#     # 파이썬에서는 제3의 변수 둘필요 없이 바로 바꿔치기 가능
#     list[i-1],list[j-1] = list[j-1],list[i-1]
# for i in range(N):
#     print(list[i], end=' ')

# N,M=map(int, input().split())
# list=[i for i in range(1,N+1)]
# for i in range(M):
#     i,j=map(int, input().split())
#     myList=list[i-1:j]
#     myList.reverse()
#     list[i-1:j]=myList
# for i in range(N):
#     print(list[i], end=' ')

# print(len(input()))

# a = input()
# print(ord(a))
# ord(문자)
# 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환

# S = list(input())
# c = 'abcdefghijklmnopqrstuvwxyz'
# for a in c:
#     if a in S:
#         print(S.index(a), end =' ')
#     else:
#         print(-1, end=' ')

# s = int(input())
# for _ in range(s):
#     cnt, printing = input().split()
#     for s in printing:
#         print(s*int(cnt), end='')  
#     print()

# 2+h-1=h+1

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# msg = input()  # 입력받는 단어
# totalNum = 0 # 시간합계
# for j in range(len(msg)): # msg의 첫번째 알파벳부터 1개씩 돌면서
#     for i in dial: # dial에 포함되는지 첫번째ABC부터 8를 다 돈다
#         if msg[j] in i: # 해당문자가 포함되면
#             totalNum += dial.index(i)+3 # 그 인덱스(문자열이 2시 위치부터 존재하니까 +3)
# print(totalNum)

# a=str(input())
# # reversed() 함수는 이터레이터를 반환하기 때문에 문자열과 직접 비교할 수 없음
# if a == a[::-1]:
#     print ("1")
# else :
#     print ("0")


a=str(input())
b=str(a.lower())
alphabetSet = set()
 # 키,값으로 저장하려면 딕셔너리로 받아야함
 # fromkeys : 딕셔너리에 키값만 주려면
alphabetNum = dict.fromkeys(alphabetSet,0) # 딕셔너리
for i in b:
    if i.isalpha(): # # 문자가 알파벳인지 확인
        alphabetSet.add(i) # 알파벳이면 set에 집어넣는다(중복이 안생김)
        alphabetNum[i] = 0 # 이때 각 알파벳마다 딕셔너리를 초기화시켜줘야함
for alphabet in b:
    for setAlpha in alphabetSet:
        if alphabet in alphabetSet:
            alphabetNum[alphabet] += 1
max_count = max(alphabetNum.values())
        
if len(max(alphabetNum))>=2:
    print("?")
else:
    print({alphabetNum[alphabet]}.upper())