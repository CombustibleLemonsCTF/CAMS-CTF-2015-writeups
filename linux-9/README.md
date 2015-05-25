# CAMS CTF 2015: Linux 9

### Problem

**Points**: 200

**Description**: 

> Notice a secret?

**Hint**: 

None given.

### Solution

After more searching, we looked inside `/home`, where Linux stores personal user files, and found that there was an additional directory named `flag` that is not readable. However, according to `linuxuser123`'s `.bash_history`, we know that `linuxuser123` probably already has `sudo` (superuser) powers. Sure enough, we can root using `sudo su` and read the flag in `/home/flag/flag.txt`.

**Flag**: `{r00t_0nlY}`

### Other Resources

* None.
