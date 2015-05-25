# CAMS CTF 2015: Linux 7

### Problem

**Points**: 125

**Description**: 

> Anything suspicious?

**Hint**: 

None given.

### Solution

When we examined `.bash_history` in [Linux 6](../linux-6), we noticed that `linuxuser123` installed Apache 2 using `pacman` (the package manager), changed into the directory `/srv/http`, and edited `index.html` there. Sure enough, `index.html` contains the flag.

**Flag**: `{l0calh0sts}`

### Other Resources

* None.
