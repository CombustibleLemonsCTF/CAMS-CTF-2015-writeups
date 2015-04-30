# CAMS CTF 2015: Crypto 1

### Problem

**Points**: 10

**Description**: 

> Spiders planted in some computers have recently pulled out a bunch of data regarding the communication of The Ninteenus and its entourage. Our horrible cryptographers could not figure out what they were saying. I'm sure you could do a better job.  
> crypto_1.txt

**Hint**: 

None given.

### Solution

```
[!] cat crypto-1/crypto_1.txt 
01001001 00100000 01110100 01101000 01101001 01101110 01101011 00100000 01001001 00100111 01101101 00100000 01100010 01100101 01101001 01101110 01100111 00100000 01110111 01100001 01110100 01100011 01101000 01100101 01100100 00101110 00100000 01000110 01101111 01110010 00100000 01101110 01101111 01110111 00101100 00100000 01001101 01110010 00101110 00100000 01000010 01110010 01101111 01110111 01101110 01101001 01101110 01100111 00101100 00100000 01101100 01100101 01110100 00100000 01110101 01110011 00100000 01100011 01101111 01101101 01101101 01110101 01101110 01101001 01100011 01100001 01110100 01100101 00100000 01101001 01101110 00100000 01111011 00110111 01101000 00110001 01110011 01011111 00110001 01101110 01110000 00110011 01101110 00110011 00110111 01110010 00110011 01100010 01101100 00110011 01011111 01100011 00110000 01100100 00110011 01111101 00101110 00100000 00001101 00001010 01001110 01101001 01101110 01110100 01100101 01100101 01101110 01110101 01110011 00100000 01001111 01110101 01110100 00101110 00100000
```

As shown, `crypto_1.txt` contains strings of 8-bit binary numbers. If you do not know what binary numbers are, [this](http://mathworld.wolfram.com/Binary.html) is a pretty good start.

The standard for converting between numbers and characters and vice versa is [ASCII](http://en.wikipedia.org/wiki/ASCII) (the American Standard Code for Information Interchange); almost all languages use this coding scheme. The flag can be obtained by converting each binary string into a base-10 number, retrieving the character associated with that number, and then putting all of the characters together. Here is a Python two-liner: 

```
[!] python3
Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
[GCC 4.8.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = open('crypto_1.txt', 'r').read().strip().split(' ')
>>> print(''.join(chr(int(s, 2)) for s in a))
I think I'm being watched. For now, Mr. Browning, let us communicate in {7h1s_1np3n37r3bl3_c0d3}. 
Ninteenus Out.
```

**Flag**: `{7h1s_1np3n37r3bl3_c0d3}`

### Other Resources

* None.
