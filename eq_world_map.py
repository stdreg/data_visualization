import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_all_month.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
magnitudes, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])

#map the ear
data = [Scattergeo(lon=longitudes, lat=latitudes)]
my_layout = Layout(title='Global Eqarthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig,  filename='data/global_earthquakes.html')