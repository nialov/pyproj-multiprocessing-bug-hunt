"""
Script to recreate pyproj 3.2.0 multiprocessing bug.
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
import pyproj

results = []
with ProcessPoolExecutor() as executor:
    for i in range(10):
        results.append(executor.submit(pyproj.CRS, "EPSG:3067"))

for process in as_completed(results):
    print(process.result())
