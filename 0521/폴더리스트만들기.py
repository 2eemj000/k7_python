# https://blockdmask.tistory.com/554

# 현재 위치에 폴더 만들기
# import os
# folder_name1 = "MyFolder1"
# os.mkdir(folder_name1)  # 따로 경로 입력하지 않고 폴더명만 입력


# folder_name2 = "MyFolder2"
# current_path = os.getcwd()  # 현재 경로 가지고오기
# os.mkdir(current_path + "/" + folder_name2)  # 현재 경로 + 폴더명 입력

import os

# 폴더 확인 함수
def check_folders(base_path, folder_prefix, start, end):
    for i in range(start, end + 1):
        folder_path = os.path.join(base_path, f"{folder_prefix}{i}")
        if os.path.exists(folder_path):
            print(f"{folder_path} exists.")
        else:
            print(f"{folder_path} does not exist.")

# 기본 경로 및 폴더 접두사 정의
base_path = "new_folder/new_new_folder"
folder_prefix = "GoodFolder"

# 폴더 생성 코드 (기존 코드와 동일)
os.makedirs(base_path, exist_ok=True) # 폴더 안에 폴더를 만들게
# os.makedirs("경로/폴더1/폴더2/폴더3")
# os.makedirs("/폴더1/폴더2/폴더3")
# os.makedirs(" 경로/폴더~~~", exist_ok=True)

os.mkdir(os.path.join(base_path, "GoodFolder1")) # 폴더를 생성
os.mkdir(os.path.join(base_path, "GoodFolder2"))
os.mkdir(os.path.join(base_path, "GoodFolder3"))

num = 4 # for문 돌려서 폴더를 여러개 한꺼번에 만들 수 있음
while num < 5:
    os.mkdir(os.path.join(base_path, f"{folder_prefix}{num}"))
    num += 1

# 생성된 폴더 확인
check_folders(base_path, folder_prefix, 1, 9)