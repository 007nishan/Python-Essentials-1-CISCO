import os
import csv
from gmplot import gmplot


gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv', 'r') as file:
    reader = csv.reader(file)
    k = 0
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        if k == 0:
            gmap.marker(lat, lon, 'cornflowerblue')
            k = 1
        else:
            gmap.marker(lat, lon, 'blue')

gmap.marker(lat, lon, 'red')
gmap.draw("mymap.html")

