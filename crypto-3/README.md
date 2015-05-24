# CAMS CTF 2015: Crypto 3

### Problem

**Points**: 25

**Description**: 

> Continued from Crypto 2.  
> crypto_3.txt

**Hint**: 

None given.

### Solution

The message appears to have been encoded using [Base64](http://en.wikipedia.org/wiki/Base64), a method of safely transferring binary data as ASCII. Any Base64 decoder will suffice.

```
[!] cat crypto-3/crypto_3.txt | base64 -d 
Give me a situation report on the progress of our most recent venture. If this is not successful we can kiss our government grants goodbye. {d0_N07_f41!_^^3}
Panadero AFK.
```

**Flag**: `{d0_N07_f41!_^^3}`

### Other Resources

* None.
