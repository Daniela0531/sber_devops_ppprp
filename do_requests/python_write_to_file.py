import os
import requests


try:
    statistics = requests.get(f'http://app:3000/statistics')
    time_and_statistics = statistics.text + "\n"
    with open("/data/statistics.txt", "a") as file:
        file.write(time_and_statistics)
except Exception as e:
    print(str(e))

