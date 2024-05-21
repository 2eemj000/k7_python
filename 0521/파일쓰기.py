from pathlib import Path
import os
print(f"현재경로 = {os.getcwd()}")

# 파일 생성 및 쓰기
with open('파이썬으로 만든 파일1.txt', 'w') as file: # file변수는 open된 객체
    file.write("Hello, World!\n") # 교재처럼 file.write_text() 메소드가 없음
    file.write("This is a new line.\n")
   

print("File created and written successfully.")

path = Path('파이썬으로 만든 파일1.txt') # 파일로 경로 설정하면 
path.write_text("! Adding a new line with path method ! \n") # write_text() 메소드 생김 # 맨 위에 추가해줌
with path.open('a', encoding='utf-8') as file: # 다음 줄에 추가해줌 (윗줄이랑 차이)
    file.write('! 한글로 추가하려면 encoding 필요 !\n')

# 파일에 내용 추가하기
with open('파이썬으로 만든 파일1.txt', 'a') as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open('파이썬으로 만든 파일2.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")