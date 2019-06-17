import folium
import pandas as pd

df = pd.read_csv('Volcanoes_USA.txt')

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=6, tiles='Stamen Terrain')


def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - min(df['ELEV'])) / 3)
    if elev in range(minimum, minimum + step):
        col = 'green'
    elif elev in range(minimum + step, minimum + step * 2):
        col = 'orange'
    else:
        col = 'red'
    return col


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name + "\n(" + str(elev) + ")", icon=folium.Icon(color=color(elev))).add_to(map)

map.save('test.html')
