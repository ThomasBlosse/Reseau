# TP OPENSSL


## ----------PARTIE 3 - CODAGE EN BASE64----------


### Exercice 2.1

texte à encoder : message à encoder, pas trop long, ni trop court

openssl enc -base64 -in test.txt -out test_encode.txt

texte encodé : bWVzc2FnZSDDoCBlbmNvZGVyLCBwYXMgdHJvcCBsb25nLCBuaSB0cm9wIGNvdXJ0Cg==

openssl enc -base64 -d -in test_encode.txt -out test_decode.txt

texte décodé : message à encoder, pas trop long, ni trop court



### Exercice 2.2 

Non ce n'est pas une bonne méthode, on vient de le démontrer qu'il est facilement possible de décoder un message encodé en base 64.


## ----------PARTIE 3 - FICHIERS DE MOTS DE PASSE----------

### Exercice 3.1

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ sudo adduser pass1
Adding user `pass1' ...
Adding new group `pass1' (1001) ...
Adding new user `pass1' (1001) with group `pass1' ...
Creating home directory `/home/pass1' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for pass1
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
chfn: name with non-ASCII characters: ''
Is the information correct? [Y/n] y


sudo cat /etc/shadow
pass1:$6$8iE5d8wpuZLydZ41$pdsmhuvH5Jksa0UDrDV.HomowdqDAcjCTwW/CxzclpLjFGF2KtURlXmLbGujcklXedXV/XqzArCuM/wx7dwwU1:19997:0:99999:7:::



### Exercice 3.2

Pour afficher mon système d'exploitation linux a directement encodé le mot de passe lui même et on n'a pas pu choisir l'encodage voulut alors on a continuer la question en créant des mots de passe quelconques.

Chiffrement avec DES :

openssl passwd -crypt -salt ab test123
abRcsZmlrrKFA

openssl passwd -1 -salt sel motdepassesecurise
$1$sel$rjt2cnZ0pcmwPjhnM9MA6/



### Exercice 3.4

*code*


### Exercice 3.5

Si on ne dispose pas du sel, il faudra donc introduire dans notre programme une partie qui essaie tous les sels possible en commencant par les sel d'un caractère pui de deux etc... ce qui augmente exponentiellement la complexité de notre programme. Ce qui montre que l'introduction du sel dans le chiffrement ou le hachage augmente grandement la sécurité. 




## ----------PARTIE 4 - CHIFFREMENT----------

### Exercie 4.1 

texte à encoder : message à encoder, pas trop long, ni trop court

openssl enc -des -base64 -pbkdf2 -in test.txt -out test_encode.txt -k mdp

J'ai ajouté l'argument -pbkdf2 car sans mon terminal m'affichait l'erreur :
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.

texte encodé avec DES : U2FsdGVkX18+Iq6IoQzbtpEJaNRC5E14NmJUR1qtnfcLre0QEVW7Wd24GVK8m8F5
znh2msECxfZOATG34aqPyM+VP0WhnW5j

texte décodé : message à encoder, pas trop long, ni trop court



### Exercice 4.2

essai de décodage avec le mauvais mot de passe : 
openssl enc -des -d -base64 -pbkdf2 -in test_encode.txt -out test_decode.txt -k aaa
bad decrypt
140212303529280:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:610:



### Exercice 4.3 

Le fichier test.txt (le fichier clair) fait 49 bits tandis que le fichier test_encode.txt (fichier chiffré) fait 98 bits, soit le double de la taille du fichier original.



### Exercice 4.4

openssl enc -des -base64 -pbkdf2 -in f1.txt -out f1_encode.txt -k mdp -nopad
openssl enc -des -base64 -pbkdf2 -in f2.txt -out f2_encode.txt -k mdp -nopad

en utilisant -nopqd, il faut que le fichier ait une taille de multiple de 8 sinon on se retrouve avec l'erreur : 
bad decrypt
139661506532672:error:0607F08A:digital envelope routines:EVP_EncryptFinal_ex:data not multiple of block length:../crypto/evp/evp_enc.c:445:

openssl enc -des -d -base64 -pbkdf2 -in f1_encode.txt -out f1_decode.txt -k mdp -nopad

openssl enc -des -d -base64 -pbkdf2 -in f2_encode.txt -out f2_decode.txt -k mdp -nopad


f1 : ceci est le premier fichier f1, il sera utilisé pour le test de la question 4.4
f1_encode : 
U2FsdGVkX1/EE8K/BqeVWMf6G9cqEilU2BwhgJQNhn9k+k7pA3Spb1drF08VEx9R
I3htAOs8WBpyRr528ni4U9KV3l0TTmPxW3enc/j+Edr/TR8/Ibup15Fmn0en5Bbg
f1b : ceci est le premier fichier f1, il sera utilisé pour le test de la question 4.4

f2 : fichier f2 tout pareil mais different que le premier
f2_decode : U2FsdGVkX187bYpThllc9nXDnHpZZ16+4w3ASs0ByOMTmJV/8W4iXtj8Rvpd+g9q
f2b : fichier f2 tout pareil mais diff



### Exercice 4.5

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ xxd f1.txt
00000000: 6365 6369 2065 7374 206c 6520 7072 656d  ceci est le prem
00000010: 6965 7220 6669 6368 6965 7220 6631 2c20  ier fichier f1, 
00000020: 696c 2073 6572 6120 7574 696c 6973 c3a9  il sera utilis..
00000030: 2070 6f75 7220 6c65 2074 6573 7420 6465   pour le test de
00000040: 206c 6120 7175 6573 7469 6f6e 2034 2e34   la question 4.4

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ xxd f1b.txt
00000000: 6365 6369 2065 7374 206c 6520 7072 656d  ceci est le prem
00000010: 6965 7220 6669 6368 6965 7220 6631 2c20  ier fichier f1, 
00000020: 696c 2073 6572 6120 7574 696c 6973 c3a9  il sera utilis..
00000030: 2070 6f75 7220 6c65 2074 6573 7420 6465   pour le test de
00000040: 206c 6120 7175 6573 7469 6f6e 2034 2e34   la question 4.4

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ xxd f2.txt
00000000: 6669 6368 6965 7220 6632 2074 6f75 7420  fichier f2 tout 
00000010: 7061 7265 696c 206d 6169 7320 6469 6666  pareil mais diff
00000020: 6572 656e 7420 7175 6520 6c65 2070 7265  erent que le pre
00000030: 6d69 6572 0a                             mier.

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ xxd f2b.txt
00000000: 6669 6368 6965 7220 6632 2074 6f75 7420  fichier f2 tout 
00000010: 7061 7265 696c 206d 6169 7320 6469 6666  pareil mais diff



### Exercice 4.6

chiffrement avec mdp comme mot de passe :
openssl enc -des -base64 -pbkdf2 -in f3.txt -out f3_encode.txt -k mdp -nopad

Déchiffrement avec mdpaa comme mauvais mot de passe :
openssl enc -des -d -base64 -pbkdf2 -in f3_encode.txt -out f3b.txt -k mdpaa -nopad

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ xxd f3b.txt
00000000: 24ff 5b20 b868 0d54 908f cbd5 ddc2 18c4  $.[ .h.T........
00000010: 897c 205c f391 36f1 677a 5a1b 2c4d ff4c  .| \..6.gzZ.,M.L
00000020: fd16 e5a1 a4ed 16c1                      ........

f3b a été déchiffré de manière incorrect car on remarque beaucoup d'incohérence tel que des points qui se répètent, des caractères hexadécimaux aléatoires à des positions également aléatoire. 



## ----------PARTIE 5 - RSA----------

### Exercice 5.1

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl genrsa -out mySmall.pem 50
Generating RSA private key, 50 bit long modulus (2 primes)
140319829599552:error:04081078:rsa routines:rsa_builtin_keygen:key size too small:../crypto/rsa/rsa_gen.c:78:

Le message retourné indique qu'une taille de 50 bits est trop courte pour la génération d'une clé RSA et lorsque j'ouvre le fichier, je me retrouve avec un fichier vide ce qui indique que la clé n'a pas été généré.
La taille minimale conseillée est 512 bits alors on a créé une clé RSA de taille 512 au lieu de 50.

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl genrsa -out mySmall.pem 512
Generating RSA private key, 512 bit long modulus (2 primes)
....................+++++++++++++++++++++++++++
....+++++++++++++++++++++++++++
e is 65537 (0x010001)



### Exercice 5.2

Commande et retour pour afficher les informations de la clé privée de 512 bits :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -in mySmall.pem -text -noout
RSA Private-Key: (512 bit, 2 primes)
modulus:
    00:a9:2e:27:8e:11:93:0b:63:45:e1:c4:bb:58:fc:
    8a:90:f5:38:81:eb:ca:5a:37:f3:c5:9c:0e:d1:dc:
    22:84:8a:70:67:bb:f9:10:28:16:9b:be:5d:cb:19:
    10:3c:4b:12:c0:b7:dc:0c:d5:01:67:08:d2:f0:da:
    e3:28:39:c8:75
publicExponent: 65537 (0x10001)
privateExponent:
    5d:f1:02:07:d2:5c:6b:5b:61:87:7e:fd:64:e9:3e:
    6c:45:ae:6d:fe:27:2b:b7:9c:06:23:a4:db:05:38:
    a9:8d:6a:98:53:de:d7:09:66:60:2a:a9:f8:c6:9a:
    e3:8d:eb:ac:38:7c:78:09:b6:5b:84:c9:e3:f3:88:
    30:04:6d:b5
prime1:
    00:d8:4b:4c:69:b7:56:c5:2b:8b:3d:d3:9f:82:e9:
    57:45:98:b9:74:f0:a9:22:53:b7:b7:b3:cd:13:31:
    81:18:3b
prime2:
    00:c8:3c:bf:fc:8f:b8:ca:cf:a5:75:7f:a4:3d:b2:
    73:27:f7:5c:99:84:5e:40:4c:ee:17:0c:31:e8:0d:
    c3:47:0f
exponent1:
    69:eb:c6:09:e7:4c:c8:d5:e0:24:70:e4:26:99:da:
    b1:2c:6f:75:c2:fd:30:e0:4a:91:dd:ad:49:fe:ee:
    37:4d
exponent2:
    00:a0:9f:32:b6:4b:27:c5:f0:99:5e:4e:9c:96:2d:
    3e:78:b1:d1:63:08:2e:7e:cf:f7:31:1f:c4:2c:cc:
    55:77:fb
coefficient:
    4f:b9:53:62:2c:47:37:c6:9c:49:0e:a3:c8:76:64:
    74:8d:34:bf:22:5a:25:80:d1:8a:06:ed:95:d1:f8:
    0e:7f



### Exercice 5.3

Non il ne faut pas conserver la clé privée en clair car elle serait très vulnérable à une attaque. La clé privée que l'on vient de générer est sauvegarder en clair.



### Exercice 5.4

*programme*



### Exercice 5.5

Sûrement car elle est petite ptdr.



### Exercice 5.6

Commande pour créer la clé private1.pem de 1024 bits sans chiffrement :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl genrsa -out private1.pem 1024
Generating RSA private key, 1024 bit long modulus (2 primes)
.......+++++
..........+++++
e is 65537 (0x010001)


Commande pour créer la clé private2.pem de 1024 bits avec chiffrement :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl genrsa -des3 -out private2.pem 1024
Generating RSA private key, 1024 bit long modulus (2 primes)
..............+++++
.+++++
e is 65537 (0x010001)
Enter pass phrase for private2.pem:
Verifying - Enter pass phrase for private2.pem:

Pour la création de la clé privé chiffrée avec triple DES on nous demande une "pass phrase", on a saisit la "pass phrase" : mdp1 (qui est d'ailleurs de longueur minimum pour un pass phrase).



### Exercice 5.7

Commande et retour pour afficher les informations sur la clé privée 1 : 

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -in private1.pem -text -noout
RSA Private-Key: (1024 bit, 2 primes)
modulus:
    00:e0:01:f9:4c:cb:54:92:0a:3a:e7:c6:46:27:a4:
    07:53:b3:d8:e9:11:ea:56:a0:1b:37:bf:4a:2d:76:
    9d:d9:3f:93:9c:9a:8d:b1:ad:d2:85:90:90:4f:56:
    04:c3:d3:df:89:20:32:ef:d2:ea:c5:f5:25:7b:65:
    e1:ab:c8:53:c4:17:49:03:35:90:d1:b1:f7:f6:20:
    76:45:fb:fc:21:ae:8f:04:0a:6f:0a:4a:b5:67:4d:
    39:0c:aa:3a:42:99:d7:11:a5:5d:07:2a:dc:5b:54:
    2b:50:5f:60:bd:1c:b4:84:7a:e6:c8:44:c5:b3:45:
    06:29:51:c5:fe:73:5c:f6:df
publicExponent: 65537 (0x10001)
privateExponent:
    27:48:91:54:a3:4f:c8:70:9c:d5:ea:92:80:ff:25:
    fd:ca:cb:5e:4c:33:01:50:00:95:ed:28:f0:02:1e:
    3a:6c:08:d1:ec:d4:ae:75:22:37:24:1b:fa:9d:c6:
    26:25:70:cd:16:65:78:63:4f:a2:b9:94:02:28:e2:
    c3:82:55:15:f9:48:3f:30:fd:a6:9b:92:2f:4b:f6:
    16:2b:69:b8:e0:db:2c:e4:ae:df:87:3d:68:6b:6c:
    17:0d:69:59:54:20:9b:70:cc:9d:c7:7a:a1:0c:b5:
    d9:d3:c9:aa:54:54:20:6a:95:2e:f8:ed:a5:a8:2e:
    4c:de:c9:c6:d1:f3:38:d9
prime1:
    00:f8:0f:57:dd:4e:b6:85:ee:c7:cc:14:b0:47:65:
    f9:0b:04:98:4d:c1:d5:c3:25:43:fe:1f:73:d6:ef:
    c8:6e:15:a2:74:f5:f1:c6:ac:b7:ee:3b:09:cd:17:
    de:47:a3:d9:0f:c9:cf:f2:e4:5f:5c:13:4c:db:d2:
    34:72:8b:04:2d
prime2:
    00:e7:2d:8a:9e:4a:e4:26:34:5f:c0:d9:5f:ad:c5:
    e2:e8:30:75:c3:7f:6d:31:73:96:f6:2b:4b:69:19:
    8b:cd:39:6f:b1:3c:97:e5:25:5b:a5:0b:53:be:60:
    85:f5:1b:9c:ad:e0:e7:e0:fa:c6:3f:98:df:10:9c:
    8c:82:74:d2:bb
exponent1:
    18:8f:a4:5a:84:45:ac:43:35:43:2e:b5:39:8c:8e:
    39:1a:0e:5e:7c:97:c6:c7:b4:d0:bf:9a:7f:a8:a4:
    46:ca:1b:98:cb:15:52:5f:9d:a2:97:f3:e3:7b:be:
    85:87:62:a1:9e:90:d9:72:e5:42:3f:a2:f7:8c:fb:
    a6:6f:bf:4d
exponent2:
    00:de:83:b6:5e:40:85:b3:c4:4b:ba:4b:40:cd:f9:
    a0:3b:8f:91:7a:98:27:99:26:c2:52:b6:3f:82:ad:
    25:24:67:39:7b:e6:6f:ea:0e:f8:54:37:3f:e7:09:
    ef:46:8a:ca:57:8f:18:82:33:bf:28:ad:d3:5f:a0:
    df:9a:1e:2a:4b
coefficient:
    00:b4:bf:57:0c:0e:82:bf:f7:f5:26:2c:13:74:95:
    1a:db:2a:f4:93:60:88:4c:60:34:6e:91:ac:23:78:
    07:58:31:95:80:63:21:b2:8c:4b:7a:36:23:97:b6:
    8c:0a:13:15:dc:60:02:25:4c:90:03:ef:e9:5a:92:
    69:ad:5d:ee:08


Pour la deuxième clé privée il faut entrer le mot de passe (mdp1) pour pouvoir accéder aux informations. Commande et retour : 

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -in private2.pem -text -noout
Enter pass phrase for private2.pem:
RSA Private-Key: (1024 bit, 2 primes)
modulus:
    00:b6:48:43:7d:45:a6:e6:1b:2c:75:88:2e:ef:c6:
    5b:ec:39:21:4a:f2:77:79:37:2f:a1:4b:ac:ee:d9:
    69:8f:f9:e8:62:5e:20:49:e6:4d:eb:1b:c0:78:44:
    df:f2:94:03:e3:5d:5e:9b:e0:cb:6e:f0:9c:1d:3f:
    06:fa:ca:67:72:f0:18:43:1e:06:5e:87:72:b2:94:
    7c:48:18:d2:9d:e2:ea:10:98:90:c8:af:f4:d0:4f:
    e4:b0:00:e8:06:7e:5b:7e:32:9c:92:8d:7f:94:ab:
    e2:df:f1:73:99:f7:e6:7d:ac:8c:28:e9:d1:ef:4b:
    a3:28:9e:57:99:3c:ad:cf:21
publicExponent: 65537 (0x10001)
privateExponent:
    16:03:b6:3a:eb:ed:93:3e:d6:e8:be:f0:c4:3e:95:
    9d:7a:ec:dd:6b:59:28:87:94:b6:0b:38:b0:84:0b:
    6e:bb:04:e8:d4:6b:5b:e1:77:a9:9c:69:6b:5d:0e:
    1a:f2:eb:61:4b:46:80:d6:ee:5a:d0:ae:5a:0d:e1:
    9e:ea:51:01:e9:5a:9a:86:8c:3c:4c:b8:cf:ea:47:
    cf:81:5f:0e:2a:52:07:68:31:04:06:f1:cb:b6:eb:
    2a:24:f5:47:04:60:98:93:22:e5:da:83:04:08:61:
    db:94:b0:67:63:ca:52:80:bb:a8:91:c8:97:fe:1f:
    0d:b1:42:9f:f1:e9:3c:11
prime1:
    00:e6:31:55:62:0c:7c:d4:c1:77:c0:e9:e5:74:43:
    56:c2:69:0f:29:d0:a8:6d:7e:e5:6f:a4:63:2e:d3:
    15:db:53:57:68:b7:df:96:63:d6:f9:22:d2:3a:f7:
    49:29:c6:d2:f6:cf:3b:47:9d:59:ab:c6:45:84:98:
    e8:f0:cf:00:75
prime2:
    00:ca:b7:df:5e:69:e4:83:66:fb:02:6a:0f:49:8f:
    11:00:fe:b3:ab:dd:c7:2f:bd:47:52:c8:b0:f3:de:
    05:71:ea:12:cf:15:dc:9c:52:ef:1b:41:8f:09:93:
    b2:92:e1:23:17:58:8e:5e:05:0b:ea:17:0c:09:98:
    5a:d3:bd:7e:7d
exponent1:
    40:81:60:98:da:40:fc:e9:be:22:2c:29:25:7c:5d:
    4a:9b:60:29:6a:94:58:22:b0:2e:a9:d5:35:60:e7:
    86:0f:83:b6:0f:98:b3:2f:05:25:c9:71:3a:1e:e3:
    bc:b6:3f:95:f4:1a:7b:86:07:83:d0:4a:d8:ce:74:
    b0:4e:81:a5
exponent2:
    7f:61:6c:f5:69:ba:d2:aa:fa:1d:39:41:e3:ea:07:
    38:45:d3:e6:b2:14:40:b6:42:44:0d:a1:cb:8b:7e:
    86:67:1c:6c:8e:03:33:23:95:e5:dd:9b:20:dc:73:
    40:82:41:c7:a0:b8:cc:f1:84:dc:12:a1:58:c2:28:
    88:96:b1:0d
coefficient:
    4f:8f:15:dd:df:ff:e1:78:51:95:42:d6:fa:3e:e5:
    a9:f4:8e:d3:f0:95:e8:20:b2:85:65:ff:76:45:de:
    90:db:42:d4:6c:c0:2f:a3:82:7c:76:ae:ac:83:9b:
    23:f8:b1:93:4d:e6:e5:c7:de:a9:fd:b7:b6:6f:f4:
    81:b6:2e:d5

Comme attendu du chiffrement on nous demande la pass phrase pour pouvoir accéder à la clé privée. 



### Exercice 5.8

Commande pour créer une clé publique associée à la clé privée 1 :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -in private1.pem -pubout -out public1.pem
writing RSA key

Commande pour créer une clé publique associée à la clé privée 2 :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -in private2.pem -pubout -out public2.pem
Enter pass phrase for private2.pem:
writing RSA key



### Exercice 5.9 

Oui il faut conserver la clé publique en clair car comme son nom l'indique elle est publique et donc tout le monde doit pouvoir la voir. Notre clé publique est bien en claire.



### Exercice 5.10

Informations de la première clé publique :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -pubin -in public1.pem -text -noout
RSA Public-Key: (1024 bit)
Modulus:
    00:e0:01:f9:4c:cb:54:92:0a:3a:e7:c6:46:27:a4:
    07:53:b3:d8:e9:11:ea:56:a0:1b:37:bf:4a:2d:76:
    9d:d9:3f:93:9c:9a:8d:b1:ad:d2:85:90:90:4f:56:
    04:c3:d3:df:89:20:32:ef:d2:ea:c5:f5:25:7b:65:
    e1:ab:c8:53:c4:17:49:03:35:90:d1:b1:f7:f6:20:
    76:45:fb:fc:21:ae:8f:04:0a:6f:0a:4a:b5:67:4d:
    39:0c:aa:3a:42:99:d7:11:a5:5d:07:2a:dc:5b:54:
    2b:50:5f:60:bd:1c:b4:84:7a:e6:c8:44:c5:b3:45:
    06:29:51:c5:fe:73:5c:f6:df
Exponent: 65537 (0x10001)

Informations de la deuxième clé publique :

thomas@teclast-thomas:~/Desktop/Reseau_Securite$ openssl rsa -pubin -in public2.pem -text -noout
RSA Public-Key: (1024 bit)
Modulus:
    00:b6:48:43:7d:45:a6:e6:1b:2c:75:88:2e:ef:c6:
    5b:ec:39:21:4a:f2:77:79:37:2f:a1:4b:ac:ee:d9:
    69:8f:f9:e8:62:5e:20:49:e6:4d:eb:1b:c0:78:44:
    df:f2:94:03:e3:5d:5e:9b:e0:cb:6e:f0:9c:1d:3f:
    06:fa:ca:67:72:f0:18:43:1e:06:5e:87:72:b2:94:
    7c:48:18:d2:9d:e2:ea:10:98:90:c8:af:f4:d0:4f:
    e4:b0:00:e8:06:7e:5b:7e:32:9c:92:8d:7f:94:ab:
    e2:df:f1:73:99:f7:e6:7d:ac:8c:28:e9:d1:ef:4b:
    a3:28:9e:57:99:3c:ad:cf:21
Exponent: 65537 (0x10001)



### Exercice 5.11

Commande pour chiffrer le petit fichier avec la clé publique : 

openssl rsautl -encrypt -in petitFichier.txt -inkey public1.pem -pubin -out petitFichierChiffre.txt

Il n'y a pas eut de problème lors du déchiffrement du texte du petit fichier.



### Exercice 5.12

Maintenant chiffrons un fichier un peu plus grand.
Code pour chiffrer le gros fichier avec la clé publique :

openssl rsautl -encrypt -in grosFichier.txt -inkey public1.pem -pubin -out grosFichierChiffre.txt


Cependant on se retrouve avec une erreur :

RSA operation error
140377877345600:error:0406D06E:rsa routines:RSA_padding_add_PKCS1_type_2:data too large for key size:../crypto/rsa/rsa_pk1.c:127:

Cette erreur dit que les données sont trop grandes. Avec un peu de recherche j'ai trouvé que RSA peut seulement crypter des petites quantité de données tel que des clés ou des mots de passe mais non pas des textes longs. 



### Exercice 5.13

Commande pour chiffrer un court message avec la clé publique de mon binôme :

openssl rsautl -encrypt -in courtMessage.txt -inkey publicBinome.pem -pubin -out courtMessageChiffre.txt


Commande pour déchiffrer un court message avec la clé privée de mon binôme :

openssl rsautl -decrypt -in courtMessageChiffre.txt -inkey privateBinome.pem -out courtMessageDechiffre.txt

Après déchiffrement on retrouve bien le message originel.



## Exercice 5.14

Commande pour chiffrer le long message avec DES et avec "dromadaire" comme mot de passe (clé DES) : 

openssl enc -des -pbkdf2 -in grosFichier.txt -out grosFichierChiffre.txt 
enter des-cbc encryption password:
Verifying - enter des-cbc encryption password:


Commande pour chiffrer le mot de passe (clé DES) avec la clé publique de mon binôme : 

openssl rsautl -encrypt -in courtMessage.txt -inkey publicBinome.pem -pubin -out courtMessageChiffre.txt


On envoie ensuite le mot de passe (clé DES) chiffré avec la clé publique et le long message chiffré avec DES. 


Commande pour déchiffrer le mot de passe avec la clé privée du binôme : 

openssl rsautl -decrypt -in mdpChiffre.txt -inkey privateBinome.pem -out mdpDechiffre.txt


Commande pour déchiffrer le texte avec le mot de passe (clé DES) déchiffré dans l'étape précédente "dromadaire" : 

openssl enc -des -d -pbkdf2 -in grosFichierChiffre.txt -out grosFichierDechiffre.txt
enter des-cbc decryption password:



## Signatures

### Exercice 5.15

Il faut utiliser la clé privée car si quelqu'un ouvre la clé il ne pourra pas la fermer et il ne pourra pas signer avec la même signature donc on saura qu'elle a été ouverte. Cela prouve également qu'on est le propriétaire de la clé privée.



### Exercice 5.16

openssl dgst -md5 -out message_hache.txt message.txt

openssl rsautl -sign -in message_hache.txt -inkey private1.pem -out signature.txt



### Exercice 5.17

openssl rsautl -verify -in signature.txt -pubin -inkey public1.pem -out message_verifie.txt

diff message_hache.txt message_verifie.txt

le terminal ne m'a rien renvoyé ce qui indique que les deux fichiers sont identiques.



### Exercice 5.18

Hachage et signature des fichiers : 

openssl dgst -md5 -out message1_hache.txt message1.txt

openssl rsautl -sign -in message1_hache.txt -inkey private1.pem -out signature1.txt

openssl dgst -md5 -out message2_hache.txt message2.txt

openssl rsautl -sign -in message2_hache.txt -inkey private1.pem -out signature2.txt

Je modifie le message2 mais je garde la même taille de fichier



On enlève la signature sur les fichiers avec la clé publique :

openssl rsautl -verify -in signature1.txt -pubin -inkey public1.pem -out message1_verifie.txt

openssl rsautl -verify -in signature2.txt -pubin -inkey public1.pem -out message2_verifie.txt


Ensuite on hache à nouveau les fichiers message : 

openssl dgst -md5 -out message1bis_hache.txt message1.txt

openssl dgst -md5 -out message2bis_hache.txt message2.txt


Puis on vérifie si les fichiers hachés et les fichiers hachés avec la signature enlevée sont identiques ou pas :

diff message1bis_hache.txt message1_verifie.txt 

diff message2bis_hache.txt message2_verifie.txt 

Sauf que sur le terminal me renvoie :

1c1
< MD5(message2.txt)= 1ebb49de189519bea92a5d60c297502e
---
> MD5(message2.txt)= 38cf69d9d52b29e33e30319f3d6ed6e9

Et on remarque que les deux hachages sont complètement différents.



## ----------PARTIE 6 - CERTIFICATS----------


### Exercice 6.1

On crée d'abord une clé RSA de 1024 bits : 

openssl genrsa -out user-key.pem 1024

Generating RSA private key, 1024 bit long modulus (2 primes)
..+++++
..................+++++
e is 65537 (0x010001)


Ensuite on réalise une requête de certificat :

openssl req -new -key user-key.pem -out user-request.pem


Le terminal me demande de rentrer différentes données :

You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:Auvergne
Locality Name (eg, city) []:Aubiere
Organization Name (eg, company) [Internet Widgits Pty Ltd]:ISIMA
Organizational Unit Name (eg, section) []:.    
Common Name (e.g. server FQDN or YOUR name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:chameauatroisbosse
An optional company name []:Toal

mdp : chameauatroisbosse



### Exercice 6.2

La commande fournie sur le sujet de TP m'a renvoyé une erreur sur le terminal :

openssl x509 -in user-request.pem -text -noout

unable to load certificate
140203022374208:error:0909006C:PEM routines:get_name:no start line:../crypto/pem/pem_lib.c:745:Expecting: TRUSTED CERTIFICATE


J'ai donc utilisé la commande suivante : 

openssl req -in user-request.pem -text -noout


Et voici la visualisation de la requête de certificat :

Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = FR, ST = Auvergne, L = Aubiere, O = ISIMA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (1024 bit)
                Modulus:
                    00:df:63:6d:de:50:61:3a:2a:7f:fc:ee:8d:e4:05:
                    31:29:00:81:60:52:34:46:1c:d3:5d:ef:9b:ba:fe:
                    67:87:74:1f:3c:26:ca:53:7c:84:88:b7:98:56:1c:
                    66:1d:56:39:cd:1b:e7:f0:33:00:dd:21:6e:f5:c6:
                    41:94:3b:05:33:c7:85:b8:4a:81:36:a9:4a:b8:ef:
                    d4:67:3c:e7:d7:ed:a6:47:9e:e2:d8:ec:7c:c0:da:
                    85:dc:57:34:b3:d3:92:b3:8c:54:6b:8a:e0:81:5f:
                    4b:d5:64:a6:e4:a2:3a:e8:a0:7b:3c:83:29:1d:d5:
                    c4:94:f4:d7:aa:38:a9:97:ed
                Exponent: 65537 (0x10001)
        Attributes:
            unstructuredName         :Toal
            challengePassword        :chameauatroisbosse
    Signature Algorithm: sha256WithRSAEncryption
         53:53:c7:bc:ed:62:de:5a:e4:eb:b4:e9:a5:35:d3:ea:6c:23:
         e7:0e:4a:38:be:d5:7d:7b:ff:b4:e5:7b:ab:0e:51:71:57:16:
         c8:e1:0b:39:60:14:27:09:53:fc:8b:b7:10:6d:95:23:15:b6:
         fc:3a:c4:56:bc:42:a4:f0:33:71:ff:69:38:1a:23:63:93:2d:
         39:02:43:96:aa:72:21:8a:2e:61:54:a1:1a:9f:f7:1f:b4:ac:
         7b:58:00:50:a8:aa:8a:48:08:8c:49:ff:d4:8e:08:af:b2:f3:
         3b:5e:13:9c:af:52:33:30:dd:d6:af:5f:bb:d4:a5:c9:04:36:
         21:34



### Exercice 6.3

Création d'une paire de clé pour l'autorité de certification et de la requête de certification:

openssl genrsa -out ca-key.pem 1024

Generating RSA private key, 1024 bit long modulus (2 primes)
................+++++
........+++++
e is 65537 (0x010001)


openssl req -new -key ca-key.pem -out ca-request.pem

You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:Auvergne
Locality Name (eg, city) []:Clermont-Ferrand
Organization Name (eg, company) [Internet Widgits Pty Ltd]:AC
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:dromadaireaunebosse
An optional company name []:AutCert       

mdp : dromadaireaunebosse



### Exercice 6.4

Autosignature la requête de certificat précédente : 

openssl x509 -req -in ca-request.pem -signkey ca-key.pem -out ca-certificat.pem


Retour du terminal : 

Signature ok
subject=C = FR, ST = Auvergne, L = Clermont-Ferrand, O = AC
Getting Private key



### Exercice 6.5

Visualisation du certificat *ca-certificat.pem* :

openssl x509 -in ca-certificat.pem -text -noout

Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            67:4e:2f:88:86:92:bd:29:e2:52:4f:77:c0:3c:61:50:9b:51:7d:19
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = FR, ST = Auvergne, L = Clermont-Ferrand, O = AC
        Validity
            Not Before: Oct 14 08:54:11 2024 GMT
            Not After : Nov 13 08:54:11 2024 GMT
        Subject: C = FR, ST = Auvergne, L = Clermont-Ferrand, O = AC
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (1024 bit)
                Modulus:
                    00:b2:e7:38:44:02:f6:6a:dd:e8:a7:6d:65:9f:1e:
                    40:5c:0a:51:65:33:27:2b:31:d2:0a:91:c4:ed:a9:
                    85:d0:03:4d:70:50:af:cd:19:db:b1:1f:6d:e2:12:
                    ce:70:d2:c5:d5:a0:d3:0c:5c:0b:1c:a5:4d:0c:c7:
                    76:b2:1d:ba:90:69:f2:73:b0:db:45:44:e0:2c:7a:
                    34:38:93:8e:d1:46:de:9b:69:a7:97:24:a1:e2:06:
                    04:a0:45:06:c3:52:2f:fc:fb:8e:bb:6b:de:e3:21:
                    86:96:c8:b7:0b:24:58:33:b6:1f:12:5e:ac:f9:73:
                    3b:4c:e8:1b:01:35:05:c1:7b
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
         6b:c5:f3:67:79:1b:63:41:a4:e8:c6:a5:c3:52:a8:ea:0a:31:
         57:0f:96:7b:09:98:85:d4:d4:c4:8d:56:56:29:ee:61:90:00:
         33:0c:d6:29:59:b3:43:fc:03:22:be:6a:e0:31:27:e3:14:77:
         6d:f7:77:84:3f:88:27:9a:d3:f7:d1:ce:ef:ea:a3:0c:b9:c4:
         b2:cc:69:f1:5c:00:17:cf:c4:6f:70:9b:52:4f:94:69:3e:81:
         b1:b2:ff:1e:17:46:2d:c0:1f:74:d4:3b:9b:92:c4:ce:88:05:
         86:ce:50:cd:ec:8c:58:36:d0:17:09:8b:5e:3f:f5:68:7c:ac:
         30:15



### Exercice 6.6

Création d'un fichier serial :

echo '01' > ca-serial


Signature de la requête de certificat *user-request.pem* : 

openssl x509 -days 365 -CAserial ca-serial -CA ca-certificat.pem -CAkey ca-key.pem -in user-request.pem -req -out user-certificat.pem

Signature ok
subject=C = FR, ST = Auvergne, L = Aubiere, O = ISIMA
Getting CA Private Key



### Exercice 6.7

Vérification du certificat *user-certificat.pem* :

openssl verify -CAfile ca-certificat.pem user-certificat.pem 


Retour du terminal : 

user-certificat.pem: OK

Ca indique que le certificat est vérifié.



### Exercice 6.8

Je modifie le fichier, je vérifie le certificat à nouveau : 

openssl verify -CAfile ca-certificat.pem user-certificat.pem 


Le terminal me retourne l'erreur suivante indiquant que le certificat n'est plus valide :

C = FR, ST = Auvergne, L = Aubiere, O = ISIMA
error 7 at 0 depth lookup: certificate signature failure
error user-certificat.pem: verification failed
140623681324352:error:04091068:rsa routines:int_rsa_verify:bad signature:../crypto/rsa/rsa_sign.c:220:
140623681324352:error:0D0C5006:asn1 encoding routines:ASN1_item_verify:EVP lib:../crypto/asn1/a_verify.c:170:



### Exercice 6.9

Création de l'autorité de certification CA1 :  

$openssl genrsa -out ca1-key.pem 1024

Generating RSA private key, 1024 bit long modulus (2 primes)
................+++++
...........+++++
e is 65537 (0x010001)

```
$openssl req -new -key ca1-key.pem -out ca1-request.pem

You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:GB
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:London
Organization Name (eg, company) [Internet Widgits Pty Ltd]:AutCert1GB
Organizational Unit Name (eg, section) []:.  
Common Name (e.g. server FQDN or YOUR name) []:Jones
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:GBcertification
An optional company name []:AutCert1GB  


openssl x509 -req -in ca1-request.pem -signkey ca1-key.pem -out ca1-certificat.pem

Signature ok
subject=C = GB, L = London, O = AutCert1GB, CN = Jones
Getting Private key
```

Auto signature du certificat CA1: 
```
openssl x509 -req -in ca1-request.pem -signkey ca1-key.pem -out ca1-certificat.pem

Signature ok
subject=C = GB, L = London, O = AutCert1GB, CN = Jones
Getting Private key
```



Création de l'autorité de certification CA2 : 
```
openssl genrsa -out ca2-key.pem 1024

Generating RSA private key, 1024 bit long modulus (2 primes)
........+++++
...............+++++
e is 65537 (0x010001)
```
```
openssl req -new -key ca2-key.pem -out ca2-request.pem

You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:Ile de France
Locality Name (eg, city) []:Paris
Organization Name (eg, company) [Internet Widgits Pty Ltd]:AutCert2FR
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:Martin
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:FRcertification
An optional company name []:AutCert2FR  
```

Signature de la requête de certification de CA2 avec le certificat CA1 :
```
openssl x509 -days 365 -CA ca1-certificat.pem -CAkey ca1-key.pem -CAserial ca-serial -in ca2-request.pem -req -out ca2-certificat.pem

Signature ok
subject=C = FR, ST = Ile de France, L = Paris, O = AutCert2FR, CN = Martin
Getting CA Private Key
```



### Exercice 6.10

Création d'une requête de certification avec la clé privée *user-key.pem* déjà existante : 

```
openssl req -new -key user-key.pem -out user2-request.pem

You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:Provence Alpes Cote D'azur
Locality Name (eg, city) []:Nice
Organization Name (eg, company) [Internet Widgits Pty Ltd]:NiceCertFR
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:NICEcertification
An optional company name []:NiceCertFR
```

Signature de la nouvelle requête de certification par CA2 : 
```
openssl x509 -days 90 -CA ca2-certificat.pem -CAkey ca2-key.pem -CAserial ca-serial -in user2-request.pem -req -out user2-certificat.pem

Signature ok
subject=C = FR, ST = Provence Alpes Cote D'azur, L = Nice, O = NiceCertFR
Getting CA Private Key
```



### Exercice 6.11

Vérification de la chaîne complète de certification du nouveau certificat *user-certificat.pem* :
```
openssl verify -CAfile ca1-certificat.pem -untrusted ca2-certificat.pem user2-certificat.pem
```

Sauf que le terminal me renvoie une erreur : 
```
C = FR, ST = Ile de France, L = Paris, O = AutCert2FR, CN = Martin
error 24 at 1 depth lookup: invalid CA certificate
error user2-certificat.pem: verification failed
```

