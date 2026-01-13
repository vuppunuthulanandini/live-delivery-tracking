# driver_simulator/driver.py
import requests
import random
import time

BACKEND_URL = "http://127.0.0.1:5000/update_location"

drivers = [
    {"driver_id": 101, "lat": 17.3845, "lon": 78.4866},
    {"driver_id": 102, "lat": 17.3860, "lon": 78.4875},
    {"driver_id": 103, "lat": 17.3850, "lon": 78.4855}
]

while True:
    for driver in drivers:
        driver["lat"] += random.uniform(-0.0003, 0.0003)
        driver["lon"] += random.uniform(-0.0003, 0.0003)
        data = {"driver_id": driver["driver_id"], "latitude": driver["lat"], "longitude": driver["lon"]}
        response = requests.post(BACKEND_URL, json=data)
        print(f"Sent location: {data}")
    time.sleep(2)
