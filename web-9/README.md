# CAMS CTF 2015: Web 9

### Problem

**Points**: 175

**Description**: 

> Maybe it is time to read some PHP docs.  
> Web 9

**Hint**: 

None given.

### Solution

Here is `source.php`: 

```php
<?php
error_reporting(0);

include('flag.php');
session_start();

if(!isset($_SESSION['rand0'])) {
    mt_srand(time() ^ 424242424242); // Ultra secure random seed.
    $_SESSION['rand0'] = mt_rand();
    $_SESSION['rand1'] = mt_rand();
    $_SESSION['rand2'] = mt_rand();
}

$data = "You haven't fulfilled all of my requests.";
if(isset($_POST['1']) && isset($_POST['2']) && isset($_POST['3']) && isset($_POST['4']) && isset($_POST['5'])) {
    if(strtotime(date('Y-m-d', time() + abs((int)$_POST['1']))) < strtotime('2013-12-12')) {
        if($_POST['2'] != $_POST['3'] && hash('sha512', $_POST['2']) == hash('sha512', $_POST['3'])) {
            if($_SESSION['rand0'] == $_POST['4']) {
                if(strcmp($_POST['5'], $flag) == 0) {
                    $data = $flag;
                }
            }
        }
    }
} 
?>
<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="style.css" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
        <title>Web Exploitation 9</title>
    </head>
    
    <body>
        <p>"Let's make a deal. I will give you the flag if you do 4 simple things for me." - M4gn4te Troll</p>
        <form method="post" action="index.php">
            <p>Travel back in time to a date before December 12, 2013.</p>
            <input type="text" name="1">
            <br>
            <p>Give me two strings that do not equal each other but have the same SHA-512 hash.</p>
            <input type="text" name="2">
            <input type="text" name="3">
            <br>
            <p>Guess the random number I generated before the following two numbers: <? echo $_SESSION['rand1'] . ', ' . $_SESSION['rand2'] . '.' ?></p>
            <input type="text" name="4">
            <br>
            <p>Give me the flag to this challenge.</p>
            <input type="text" name="5">
            <br>
            
            <button type="submit" style="margin-top:20px">Submit</button>
        </form>
        
        <br>
        <p style="color: #f90;"><? echo $data; ?></p>
    </body>
</html>

<!-- Source: source.php -->
```

PHP exhibits some erratic behavior when given odd inputs.

For the first component of this challenge, you can use [integer overflow](http://en.wikipedia.org/wiki/Integer_overflow) to end up with a smaller number by picking an arbitrarily large number (say, `1=10000000000000`).

Next, you can use [this behavior](https://github.com/ctfs/write-ups-2015/tree/master/boston-key-party-2015/school-bus/prudential) to exploit the second check. Make `2[]=s` and `3[]=ss`.

The random number generation isn't actually that random because the resolution of `time` is in seconds. Because you can wipe out `PHPSESSID` from the cookies and refresh the page when you choose, you can figure out the UNIX timestamp, create a test program on the client side, seed the program, and generate the numbers, including the first one.

For the last check, set `5[]=s` to screw up `strcmp` (arrays are great). 

**Flag**: Forgot what it was, but you get the idea of the solution.

### Other Resources

* None.
