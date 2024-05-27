from pathlib import Path
import csv
import plotly.express as px
from datetime import datetime

path = Path('0523/eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, cheader in enumerate(header_row):
    print(index,cheader)
lats,lons,brights,dates=[],[],[],[]
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        lat=float(row[0])
        lon=float(row[1])
        bright=float(row[2])
    except ValueError:
        print(f"missing value={current_date}") 
    else:
        dates.append(current_date)
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)
    
title = 'world_fires_1DAY'
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights, color_continuous_scale='Viridis', 
                     labels={'color':'Brights'},projection='natural earth',)
fig.show()
