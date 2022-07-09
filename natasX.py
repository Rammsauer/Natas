import requests

def natasX(x, pwd, endpoint="", headers={}, cookies={}, data={}, url="", redirect=True):
    if url != "":
        username = f"natas{x}"
        r = requests.get(url, auth=(username, pwd), headers=headers, cookies=cookies, params=data, allow_redirects=redirect)
    else:
        url = f'http://natas{x}.natas.labs.overthewire.org/{endpoint}'
        username = f"natas{x}"

        r = requests.get(url, auth=(username, pwd), headers=headers, cookies=cookies, params=data, allow_redirects=redirect)

    return r
