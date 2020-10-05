import requests


r = requests.get("http://www.blankenberge.be")
print(r.status_code)
