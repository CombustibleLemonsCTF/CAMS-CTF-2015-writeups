# CAMS CTF 2015: Web 1

### Problem

**Points**: 15

**Description**: 

> M4gn4te Troll thinks he has a really secure website. Go hack his site. We will reward you points in exchange for his secret flags.  
> Web 1

**Hint**: 

None given.

### Solution

Most web pages are formatted using [HTML](http://www.w3schools.com/html/), **H**yper-**T**ext **M**arkup **L**anguage. In HTML, items on a page, called elements, are denoted using tags, which contain the name of the element enclosed on either side by angle brackets. Most elements have an opening tag and a closing tag; a forward slash prepends the name of the element in a closing tag. For a more comprehensive overview of HTML, visit the excellent tutorial below.

Here is the source of the page, which can be obtained in Chrome by pressing <kbd>CTRL</kbd> + <kbd>U</kbd>: 

```html
<!DOCTYPE HTML>
<html>
	<head>
		<link rel="stylesheet" href="style.css" type="text/css" />
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
		<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
		<script type="text/javascript" src="scripts.js"></script>
		<title>Web Exploitation 1</title>
	</head>
	
	<body>
		<p>"Hello World! This is my first website." - M4gn4te Troll</p><!--backup:Ckwqw23-->
	
		<form action="check.php">
			<p>Password: </p>
			<input type="password" name="password"><br>
			<button type="submit" style="margin-top:20px">Submit</button>
		</form>
		
		<br>
		<p id="response"></p>
	</body>
</html>
```

Here, we can see that the password is in a comment, denoted using `<!--` and `-->`. Comments are not interpreted as code, but rather are intended to be read by people as reminders or summaries. Entering the password gives the flag.

**Flag**: `{hello_html_w0rld}`

### Other Resources

* None.
