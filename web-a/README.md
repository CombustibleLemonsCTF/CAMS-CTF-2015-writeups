# CAMS CTF 2015: Web A

### Problem

**Points**: 240

**Description**: 

> More features, more vulnerabilities, more exploitation.  
> Web A

**Hint**: 

None given.

### Solution

When we follow the link, we are confronted by Basic Authorization. After clicking cancel, we get a message from the troll: 

```
"Go away. I have extra security. The passwords are hashed and I even wrote my own PHP authorization script that connects to the database to check if the query returns only one row. You will never get in." - M4gn4te Troll
```

A database? Perhaps all of this extra security is vulnerable to [SQL injection](https://www.owasp.org/index.php/SQL_Injection)?

Setting `User Name` to `' OR 1=1 LIMIT 1 -- ` and `Password` to whatever you wish (it is commented out), we get the flag.

**Flag**: `{mY_r3alm_of_AUTHORIZATIONZ}`

### Other Resources

* None.
