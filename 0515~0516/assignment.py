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

# N은 바구니갯수, M은 공을 넣는 총 회차
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣음
# list는 변경가능한 mutable
N,M=map(int, input().split())
arr = list(range(1,N+1))
# a++라는 표현식은 파이썬에서 X, 대신에 a += 1과 같은 방식으로 사용
    # for (int a=1;a<M+1,a++):
    #     if (a>=i)&(a<=j):
    #         arr[a-1]=k
# 리스트 슬라이싱은 리스트의 일부분을 복사하여 반환하는 것이므로 단일 값을 할당하는데 사용X
# 대신에 각 인덱스를 반복하여 값을 할당해야함
    # for k in range(1, M+1):
    #     i,j=map(int, input().split())
    #     arr[range(i,j+1,1)] = k
    # print(arr)
for k in range(1,M):
    i,j= map(int, input().split())
    for idx in range(i-1, j):
        arr[idx] = k
for i in range(N):
    print(arr[i], end=' ')

    # 10810 마저 하기 ~