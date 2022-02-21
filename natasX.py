import requests

def natasX(x, pwd, endpoint="", headers={}, cookies={}, data={}):
    url = f'http://natas{x}.natas.labs.overthewire.org/{endpoint}'
    username = f"natas{x}"

    r = requests.get(url, auth=(username, pwd), headers=headers, cookies=cookies, params=data)

    return r
