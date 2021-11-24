from datetime import datetime
from time import sleep
import requests
print(datetime.now())


def check_if_up(url):
    if requests.get(url).status_code == 200:
        print(f"{url} is up and running")
    else:
        print(f"sorry, {url} is down")


check_if_up("https://www.myspace.com")


for i in range(5):
    response = requests.get("https://github.com")
    if response.status_code == 200:
        print("github is up and running")
    sleep(5)

a = 3