with open('파이썬으로 만든 파일1.txt',encoding='utf-8') as file:
  data = file.read()
  print(data)

import os
directory = os.getcwd()
flist = os.listdir(directory) # 현재 경로에 있는 폴더, 파일을 리스트로 보여줌
print(flist)