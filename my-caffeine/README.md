# CAMS CTF 2015: My Caffeine

### Problem

**Points**: 200

**Description**: 

> Please make me some coffee with 23 grams of sugar. Quickly now, before I fall asleep.  
> CCTF Coffee Machine

**Hint**: 

> 2015-04-18 > Filezilla. Not a zip. My Caffine. coffee-pot-command. That should be enough hints for today.  
> 2015-04-18 > We apologize that My Caffine is not perfect. Regardless, please just send 23 in the body when brewing. Thank you.

### Solution

In this challenge, you are tasked with understanding the coffee pot protocol, which, to quote [the specification](rfc2324.txt), is "a protocol designed espressoly for the brewing of coffee." Read the specification before anything else.

The proper order of protocols should be `BREW`, `WHEN`, `PROPFIND`, and `GET`. Here was a sample run using `cURL`, which allows you to set an arbitrary method using the `-X` flag and data using the `-d` flag: 

```
[!] curl -H "Content-Type: application/coffee-pot-command" -X BREW --cookie "PHPSESSID=vqok98o5p3p95jas1tfovr12g5" -d "23" http://coffee.camsctf.com/
<!DOCTYPE html>
<title>CCTF Coffee Machine</title>
Started brewing and adding milk.[!] curl -H "Content-Type: application/coffee-pot-command" -X WHEN --cookie "PHPSESSID=vqok98o5p3p95jas1tfovr12g5" -d "23" http://coffee.camsctf.com/
<!DOCTYPE html>
<title>CCTF Coffee Machine</title>
Stopped pouring milk. Coffee completed.[!] curl -H "Content-Type: application/coffee-pot-command" -X PROPFIND --cookie "PHPSESSID=vqok98o5p3p95jas1tfovr12g5" -d "23" http://coffee.camsctf.com/
<!DOCTYPE html>
<title>CCTF Coffee Machine</title>
AES-Encryption: SxKgRaqX; Brew-time: 1429755570[!] curl -H "Content-Type: application/coffee-pot-command" -X GET --cookie "PHPSESSID=vqok98o5p3p95jas1tfovr12g5" -d "23" http://coffee.camsctf.com/
<!DOCTYPE html>
<title>CCTF Coffee Machine</title>
+c70Xz/73+4riCRCllkBKm5MClqoTv7CUOJYtrS5LL8=
```

Now, its just a matter of AES decryption, using `SxKgRaqX` as the key and `+c70Xz/73+4riCRCllkBKm5MClqoTv7CUOJYtrS5LL8=` as the ciphertext.

**Flag**: `{htcpcp_iz_s0_real}`

### Other Resources

* None.
