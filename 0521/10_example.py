from pathlib import Path
import os
print(f"현재경로 = {os.getcwd()}")

with open('방명록.txt', 'w', encoding='utf-8') as file: 
    file.write("! 방문자 목록입니다 !\n") 


path = Path('방명록.txt')
path.write_text("0 ------------------------------ 0\n") # write_text() 메소드 생김
with path.open('a', encoding='utf-8') as file: # 다음 줄에 추가해줌 (윗줄이랑 차이)
    file.write("홍길동\n")
    file.write("금수강산\n")
