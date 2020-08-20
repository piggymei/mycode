import requests

r = requests.get('http://api.open-notify.org/astros.json')
resp = r.json()
number_people = resp["number"]


print(f"People in space: {number_people}")

for pp in resp["people"]:
    print(f"{pp['name']} on the {pp['craft']}")

