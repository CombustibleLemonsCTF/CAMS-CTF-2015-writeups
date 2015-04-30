# CAMS CTF 2015: My Background

### Problem

**Points**: 10

**Description**: 

> Notepad is your best friend.  
> black.png

**Hint**: 

None given.

### Solution

![](black.png)

This challenge was trivial. Run the above image through the `strings` command: 

```
[!] strings black.png 
IHDR
sRGB
bKGD
	pHYs
tIME
IDATx
&tEXtFlag
{iF_0nly_they_were_ALL_th1s_34sy}
IEND
```

**Flag**: `{iF_0nly_they_were_ALL_th1s_34sy}`

### Other Resources

* None.
