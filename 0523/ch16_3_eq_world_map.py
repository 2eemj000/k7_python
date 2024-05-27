from pathlib import Path
import json
import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags, # color인수는 각 포인트에 사용할 색깔을 결정하는 기준 (size인수랑 마찬가지로 mags리스트 사용)
        color_continuous_scale='Viridis', 
        labels={'color':'Magnitude'}, # labels는 딕셔너리를 받음 (색깔이 뭘 의미하는지 표시)
        projection='natural earth', # 지도의 기본디자인 정해줌 (가장자리 둥글게)
         # 각 지진의 정보를 호버텍스트에 추가함 (마우스올릴때)
    )
fig.show()