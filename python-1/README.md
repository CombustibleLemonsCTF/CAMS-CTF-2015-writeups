# CAMS CTF 2015: Python 1

### Problem

**Points**: 50

**Description**: 

> This is easy.  
> py1.py

**Hint**: 

None given.

### Solution

Python is a readable and versatile interpreted programming language that is well known for clean and consistent code. You can find the tutorial [here](https://docs.python.org/2/tutorial/).

The [program](py1.py) that we are given executes a string as Python code. We can instead [print](py1-src.py) out what gets executed: 

```python
import re;import base64
import base64
from random import randint
number = randint(0,10792579157912751097616189106168175192741851286517) 
flag = 'e24zdjNyX3VzZV9FVkFMfQ=='
input = input("I'm thinking of a number. If you guess correctly, I'll give you the flag. Enter a number: ")
if int(input) == number:
	print base64.b64decode(flag)
else:
	print 'Incorrect!'
```

Here, we already have the flag in our possession, just in a Base64-encoded form (see [Crypto 3](../crypto-3) for more information on Base64).

```
[!] echo e24zdjNyX3VzZV9FVkFMfQ== | base64 -d
{n3v3r_use_EVAL}
```

**Flag**: `{n3v3r_use_EVAL}`

### Other Resources

* None.
