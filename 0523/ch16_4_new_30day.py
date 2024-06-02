from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/new_30day.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)
all_eq_info = all_eq_data['features']
mags, lons, lats, eq_titles = [], [], [], []
for eq_info in all_eq_info:
    mag = eq_info['properties']['mag']
    lon = eq_info['geometry']['coordinates'][0]
    lat = eq_info['geometry']['coordinates'][1]
    eq_title = eq_info['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
title = "!--New 30 DAY Earthquakes--!"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags,
                     color_continuous_scale='mygbm',
                     labels={'color':'Magnitude'}, projection='natural earth', hover_name=eq_titles,)
fig.show()