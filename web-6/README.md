# CAMS CTF 2015: Web 6

### Problem

**Points**: 50

**Description**: 

> Are you a robot?  
> Web 6

**Hint**: 

None given.

### Solution

The way Google and other search engines index web pages is by using automated bots called crawlers to follow links. These crawlers are supposed to obey rules set out in a `robots.txt` file (although now these rules can be specified in the HTML itself). Sure enough, `robots.txt` is readable at the root of the site (`http://web.camsctf.com/`): 

```
User-agent: *
Disallow: /6/r0b0tz/password.txt
```

That password file looks interesting. According to `http://web.camsctf.com/6/r0b0tz/password.txt`, the password is `trekAg3j`. Entering this password in the main page form yields the flag.

**Flag**: `{no_r0b0tz_allowed}`

### Other Resources

* None.
