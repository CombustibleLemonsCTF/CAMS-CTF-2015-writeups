# CAMS CTF 2015: Crypto 2

### Problem

**Points**: 15

**Description**: 

> Continued from Crypto 1.  
> crypto_2.txt

**Hint**: 

None given.

### Solution

```
[!] cat crypto-2/crypto_2.txt 
47 6f 69 6e 67 20 74 68 72 6f 75 67 68 20 73 6f 6d 65 20 6f 66 20 6f 75 72 20 65 6d 61 69 6c 73 2c 20 49 20 68 61 76 65 20 66 6f 75 6e 64 20 73 6f 6d 65 20 73 75 73 70 69 63 69 6f 75 73 20 64 6f 63 75 6d 65 6e 74 73 20 74 68 61 74 20 68 69 6e 74 20 74 68 61 74 20 77 65 2c 20 4d 65 74 65 72 75 73 20 33 38 31 2c 20 61 72 65 20 7b 62 33 31 6e 67 5f 24 68 34 64 30 77 33 64 7d 2e 20 52 65 6d 65 6d 62 65 72 3a 20 5b 62 33 5f 73 33 63 55 72 45 5f 61 4e 64 5f 73 37 61 59 5f 73 34 66 33 5d 0d 0a 42 6c 61 63 6b 20 4f 75 74 2e 
```

This time, instead of binary numbers, the ciphertext we are given is encoded in hexadecimal, or base 16. Like in the previous problem, [Crypto 1](crypto-1), all we need to do is convert each number to ASCII.

```
[!] python3
Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
[GCC 4.8.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = open('crypto-2/crypto_2.txt', 'r').read().strip().split(' ')
>>> print(''.join(chr(int(s, 16)) for s in a))
Going through some of our emails, I have found some suspicious documents that hint that we, Meterus 381, are {b31ng_$h4d0w3d}. Remember: [b3_s3cUrE_aNd_s7aY_s4f3]
Black Out.
```

**Flag**: `b3_s3cUrE_aNd_s7aY_s4f3`

### Other Resoueces

* None.
