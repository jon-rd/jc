[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.shadow
jc - JSON CLI output utility `/etc/shadow` file parser

Usage (cli):

    $ sudo cat /etc/shadow | jc --shadow

Usage (module):

    import jc.parsers.shadow
    result = jc.parsers.shadow.parse(shadow_file_output)

Schema:

    [
      {
        "username":       string,
        "password":       string,
        "last_changed":   integer,
        "minimum":        integer,
        "maximum":        integer,
        "warn":           integer,
        "inactive":       integer,
        "expire":         integer
      }
    ]

Examples:

    $ sudo cat /etc/shadow | jc --shadow -p
    [
      {
        "username": "root",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      {
        "username": "daemon",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      {
        "username": "bin",
        "password": "*",
        "last_changed": 18113,
        "minimum": 0,
        "maximum": 99999,
        "warn": 7,
        "inactive": null,
        "expire": null
      },
      ...
    ]

    $ sudo cat /etc/shadow | jc --shadow -p -r
    [
      {
        "username": "root",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      {
        "username": "daemon",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      {
        "username": "bin",
        "password": "*",
        "last_changed": "18113",
        "minimum": "0",
        "maximum": "99999",
        "warn": "7",
        "inactive": "",
        "expire": ""
      },
      ...
    ]


## info
```python
info()
```
Provides parser metadata (version, author, etc.)

## parse
```python
parse(data, raw=False, quiet=False)
```

Main text parsing function

Parameters:

    data:        (string)  text data to parse
    raw:         (boolean) output preprocessed JSON if True
    quiet:       (boolean) suppress warning messages if True

Returns:

    List of Dictionaries. Raw or processed structured data.

## Parser Information
Compatibility:  linux, darwin, aix, freebsd

Version 1.2 by Kelly Brazil (kellyjonbrazil@gmail.com)
