from pathlib import Path
import json
import os
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents) # 데이터파일을 문자열로 읽어서 json.loads로 파이썬객체로 변환

all_eq_dicts = all_eq_data['features'] # 키를 features로 하는 value를 가져옴
print(f'지진기록의 건수 : {len(all_eq_dicts)}') # 지진기록의 건수

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # 'features'>'properties'>'mag' 이렇게 키를 가져옴
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)
    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)

title = 'earth quake'
fig = px.scatter_geo(lat=lats, lon=lons,title=title)
fig.show()

print(f'처음 10개의 지진규모 : {mags[:10]}') # 처음 10개의 지진규모
print(f'처음 10개의 경도 : {lons[:10]}')
print(f'처음 10개의 위도 : {lats[:10]}')

# # 데이터 파일을 더 읽기쉬운 형태로 바꿈
# path = Path('mapping_global_datasets/eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# # path.write_text(readable_contents)

# # Examine all earthquakes in the dataset.
# all_eq_dicts = all_eq_data['features']

# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])
