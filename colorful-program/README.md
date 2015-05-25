# CAMS CTF 2015: Colorful Program

### Problem

**Points**: 80

**Description**: 

> This is a colorful program.  
> colorful_program.pnm

**Hint**: 

None given.

### Solution

![](colorful_program.png)

According to the description, this image is a program of some kind. Since programs of color images don't seem to be that common, we can safely assume that this program is written in an [esoteric programming language](http://esolangs.org/wiki/Main_Page). A bit of Googling reveals that this program is probably written in [Piet](http://www.dangermouse.net/esoteric/piet.html).

After converting the program into a PNG, we used [this interpreter](http://wonderfl.net/c/xYU5/fullscreen) to run the program and get the flag.

Here was the output: 

```
Flag: {c0l0rbl1nd_4_lyfe}
We're serious. One of our team members is color blind.
```

**Flag**: `{c0l0rbl1nd_4_lyfe}`

### Other Resources

* None.
