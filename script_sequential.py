"""
Script to recreate pyproj 3.2.0 multiprocessing bug.
"""
import pyproj

for i in range(10):
    print(pyproj.CRS("EPSG:3067"))
