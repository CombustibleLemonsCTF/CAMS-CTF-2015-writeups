# CAMS CTF 2015: Impossible Salt

### Problem

**Points**: 50

**Description**: 

> This challenge is impossible. I promise. The flag is located at cdn.camsctf.com but its filename is the output when flag.txt is passed to salt_filename.  
> impossible_salt.py

**Hint**: 

None given.

### Solution

Upon first inspecting [the source](impossible_salt.py), it may seem like the challenge is actually impossible. You get a salt that contains a 10000-digit random number, right? Not so. This is because the there are two different variables at play here: `SALT` and `SΑLT` (notice the difference between the "A" and the uppercase Greek Alpha). Because the latter is set inside the loop and passed to `salt_filename`, there are actually only 10 possibilities, `saltystuff[0-9]` to search manually.

Note that the code in `impossible_salt.py` would only be legal in Python 3, which allows for variable names with certain Unicode characters.

```python
[!] python3
Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
[GCC 4.8.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hashlib
>>> for i in range(10):
...     salt = hashlib.sha512('saltystuff{}'.format(i).encode()).hexdigest()
...     print(hashlib.sha512((salt + 'flag.txt').encode()).hexdigest()[:50])
... 
d869a442674c2b014ed9ff9e9bb91e1ae41e07101f1c8d00c9
1e65d9504ad01f1b93e839b32865ff87d59711de9f23e89e2d
0001a431f14e35ef71dac16ba9483d7b19aa8a07b109820c12
8501a86e90c7081c8a8ca6dcd0ea78c30e198b0c4376012c4d
b91600c06720d09bfacc29ba692b930ee3df03db93943c73b2
695408562cc51a41a3833f6e598b34c10d313e222c4b7a6e84
8a3fe5bb51bca2b1d6ff462017a808ce96c3080b073cda7b59
1d039f52c3d7f5b4919f6806bd377d5044cce17b1da01ac6ec
990639e3c48002f4b8129ebca492569c77b75220dc193e87ae
f072f8e1c3ccdb81014b1aa099f2d34e74b6d0f6fe50fa2ce3
```

The flag in the file with the hashed filename when `i = 7`.

**Flag**: `{lol_unic0de_l0l}`

### Other Resources

* None.
