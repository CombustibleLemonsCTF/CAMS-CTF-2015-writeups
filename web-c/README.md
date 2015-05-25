# CAMS CTF 2015: Web C

### Problem

**Points**: 400

**Description**: 

> Imagine a world where people didn't use predictable table and column names.  
> Web C

**Hint**: 

None given.

### Solution

The main password page has nothing, but there is a quotes page. Entering `admin' -- ` as the user yields a quote, indicating that the quotes page is vulnerable to SQL injection.

Here is the source: 

```php
$reply = $database->query("SELECT * FROM [database].[table] WHERE user = '{$_POST['user']}'");
if (!$reply || mysqli_num_rows($reply) !== 1) {
	echo json_encode(array(
		'reply' => 'No data.'
	));
} else {
	$data = mysqli_fetch_row($reply);
	echo json_encode(array(
		'reply' => $data[2]
	));
}
```

After doing a bit of exploring, we discovered that we can return extra data using this query: 

```
' AND 1=0 UNION ALL SELECT 1, 2, 'Fake quote' -- 
```

where `'Fake quote'` can be other data. Now that we have a feedback system, we can start sending queries. It turns out that this database probably runs MySQL, because an `information_schema` table, which contains metadata, exists in the database. Using [this documentation](https://dev.mysql.com/doc/refman/5.0/en/information-schema.html), we can coax out the names of the tables and columns. All that is required is some careful planning.

After some investigating, we discovered that the name of the target schema is `camscsco_cctf_web_c`, the name of the target table is `s'identifier`, and the two columns are `nombre_de_usario` (username) and `kupuhipa` (password). With some proper escaping, we can retrieve the password and get the flag.

**Flag**: `{pl41n77357_b35773x7}`

### Other Resources

* None.
