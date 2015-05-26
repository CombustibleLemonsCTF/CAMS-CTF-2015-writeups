# CAMS CTF 2015: Web 5

### Problem

**Points**: 80

**Description**: 

> Disclaimer: Do not hack or engage in any non CCTF infrastructure.  
> Web 5

**Hint**: 

None given.

### Solution

Viewing the source and the cookies does not yield anything of interest. However, the troll does give some fairly specific instructions: 

```
"Getting the flag is easy. All you need to do is hack Google, pretend to be a crawler from Google, crawl onto the NSA website, hack the site, then have the site redirect the crawler to this page." - M4gn4te Troll
```

As part of a request, your browser also sends HTTP headers, which contain information about the request itself. The `User-Agent` field contains what browser and operating system you are using. This can help websites cater to your device, but, because HTTP headers can be modified, they cannot necessarily be trusted.

For example, it often costs more to connect your laptop rather than your phone to a plane's wi-fi. However, because the airline can only rely on your user agent to determine your device type, a savvy user can skirt around the price hike by changing his or her browser's user agent.

The other field relevant to this challenge is the `Referer` field (deliberately misspelled). It provides the last URL visited, but, like the other headers, it can be modified.

To solve the challenge, we need to set our user agent to that of a Googlebot (`Googlebot/2.1 (+http://www.google.com/bot.html)`) and our referer to the NSA's website URL (`https://www.nsa.gov/`). Any good browser plugin can do the trick.

**Flag**: `{hacking_g00gle_&_nsA}`

### Other Resources

* None.
