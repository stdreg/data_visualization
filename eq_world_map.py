import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_all_month.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
magnitudes, longitudes, latitudes, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['title'])

#sizes are only allowed to be positiv:
sizes = []
for mag in magnitudes:
    if mag < 0:
        sizes.append(0)
    else:
        sizes.append(mag*5)
        

#map the ear
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_text,
    'marker': {
        'size': sizes,
        'color': sizes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},        
    },
}]

my_layout = Layout(title='Global Eqarthquakes of last month')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig,  filename='data/global_earthquakes.html')