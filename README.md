# healthcheck
Check if your sites are up and running

`healthcheck.py` will search your sites for a string that should be there. If the string is found, the site is considered healthy.

It supports HTTPS and basic auth.

You have to parse to the script an INI file  as first argument with the sites you want to check. Example ini file:

```ini
[mysite]
site=http://somesite.com/
check=some string to check for inside the response. Can be utφ-8

[some-other-site-of-mine-that-needs-basic-auth]
site=http://10.8.210.250:8765/
check=Page Title
username=admin
password=password

[https-site-of-mine]
site=https://tls4life.com/
check=some string that should be inside tls4life.com
```

Example usage:

```bash
$ ./healthcheck.py healthcheck.ini 

---> 1. mysite (http://mysite.com/) -> String to check
OK

---> 2. fcdb (http://10.8.210.250:8765/) -> Some other string
Using basic auth for fcdb
OK

---> 3. fc-drom (http://somesite.info/drom.html) -> Γιου τι εφ οκτω
FAIL

---> 4. fc (http://somefc.com/alex/) -> about us
OK
```
