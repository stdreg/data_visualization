import json

filename = 'data/eq_all_month.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

#readable_file = 'data/eq_all_month_readable.geojson'
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
magnitudes, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes[:5])

