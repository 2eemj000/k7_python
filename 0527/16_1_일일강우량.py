from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('0527/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
for index, cheader in enumerate(header_row):
    print(index,cheader)
dates,highs,lows, prcps=[],[],[],[] # 빈리스트 만들기
for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high=int(row[7])
        low=int(row[8])
        prcp=float(row[5]) # 데이터는 문자열이니까 숫자로 변환
    except ValueError:
        # valueerror가 나면 그 날짜자체를 넘어감 (sitka파일로 하면 모든날짜를 다 지나가서 그래프 안그려짐)
        print(f"missing value={current_date}") 
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        prcps.append(prcp)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates, highs,color='red',alpha=0.5)
ax.plot(dates, lows, color='blue',alpha=0.5)
ax.plot(dates, prcps, color='green',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.9)
ax.set_title('sitka_weather_prcp', fontsize=24)
ax.set_xlabel('time',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('prcp',fontsize=10)
ax.tick_params(labelsize=8)
plt.show()