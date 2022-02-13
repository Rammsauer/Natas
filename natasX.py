import requests

def natasX(x, pwd, endpoint = ""):
    url = f'http://natas{x}.natas.labs.overthewire.org/{endpoint}'
    username = f"natas{x}"

    r = requests.get(url, auth=(username, pwd))

    print(r.text)
