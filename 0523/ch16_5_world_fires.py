from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('eq_data/world_fires_7_day.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, cheader in enumerate(header_row):
    print(index,cheader)
lats,lons,brights,dates=[],[],[],[]
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        lat=int(row[0])
        lon=int(row[1])
        bright=int(row[2])
    except ValueError:
        print(f"missing value={current_date}") 
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

