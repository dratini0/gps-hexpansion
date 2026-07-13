#!/usr/bin/env python3

import json
from math import pi, log, tan

from matplotlib import pyplot as plt

SCALE = 240 / 4e-5 # 240 diameter screen should fit 4e-5 mercator-radians

points = [
    ((52.038694, -2.3785), "G"),
    ((52.039473, -2.376813), "V"),
    ((52.039559, -2.378657), "A"),
    ((52.041928, -2.376643), "B"),
    ((52.040511, -2.37768), "C"),
    ((52.042087, -2.377612), "D"),
    ((52.043479, -2.376894), "0"),
    ((52.041378, -2.377571), "R"),
    ((52.040853, -2.377639), "F"),
]

lines = [
    [(52.03822, -2.37857), (52.041065, -2.377843), (52.041546, -2.377915)],
    [(52.038411, -2.377491), (52.040727, -2.376092), (52.041397, -2.375905), (52.041561, -2.376505), (52.041621, -2.377066), (52.041467, -2.378795), (52.041397, -2.380635)],
    [(52.041551, -2.377983), (52.042602, -2.376729), (52.042874, -2.376185), (52.043266, -2.37582), (52.04377, -2.375178)],
    [(52.042573, -2.376772), (52.043762, -2.377044)],
]

def mercator(point):
    lat, lon = point
    lon_mercator = round(lon / 180.0 * pi * SCALE)
    lat_mercator = round(log(tan(pi / 4 + lat / 360.0 * pi)) * SCALE)
    return (lat_mercator, lon_mercator)

points_mapped = [(mercator(point), label) for point, label in points]
lines_mapped = [list(map(mercator, line)) for line in lines]

for line in lines_mapped:
    plt.plot([lon for lat, lon in line], [lat for lat, lon in line])

for (lat, lon), label in points_mapped:
    plt.text(lon, lat, label)

plt.show()

with open("map.py", "wt") as f:
    f.write(f"points=[{json.dumps(points_mapped)}]\n")
    f.write(f"lines=[{json.dumps(lines_mapped)}]\n")
