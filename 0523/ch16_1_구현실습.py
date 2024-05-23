from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('0523/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader) # 처음부터 시작해 다음행으로 진행하도록 (한번만 호출해서 첫번째행 반환)
for index, cheader in enumerate(header_row): # enumerate : 리스트순회, 각 항목의 인덱스와 값 반환
    print(index,cheader)
dates,highs,avgs,lows=[],[],[],[] # 빈리스트 만들기
for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high=int(row[4]) # 데이터는 문자열이니까 숫자로 변환
        low=int(row[5])
        avg=int(row[3]) ### 결측치(빈 문자열을 정수로 바꿀 수 없으니까) 발생 -> 오류
    except ValueError:
        # valueerror가 나면 그 날짜자체를 넘어감 (sitka파일로 하면 모든날짜를 다 지나가서 그래프 안그려짐)
        print(f"missing value={current_date}") 
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        avgs.append(avg)
# print(highs)
# print(avgs)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates, highs,color='red',alpha=0.5)
ax.plot(dates, lows, color='blue',alpha=0.5)
ax.plot(dates, avgs, color='green',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.9)
ax.set_title('high temperature', fontsize=24)
ax.set_xlabel('time',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('temperature',fontsize=10)
ax.tick_params(labelsize=8)
plt.show()
