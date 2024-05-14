def modify_string(number):
    # s=s+"world"
    number=number+10
    print(f"함수 내 출력={number}")

# st="hello"
num=10
modify_string(num) # string을 전달하므로
print(f"함수 종료 후 출력={num}")

# int, float, string, tuple은 변경X (immutable)
# list, dictionary는 주소를 복사해서 변경하므로 변경O (mutable)