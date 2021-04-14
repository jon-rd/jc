[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.env
jc - JSON CLI output utility `env` and `printenv` command output parser

This parser will output a list of dictionaries each containing `name` and `value` keys. If you would like a simple dictionary output, then use the `-r` command-line option or the `raw=True` argument in the `parse()` function.

Usage (cli):

    $ env | jc --env

    or

    $ jc env

Usage (module):

    import jc.parsers.env
    result = jc.parsers.env.parse(env_command_output)

Schema:

    [
      {
        "name":     string,
        "value":    string
      }
    ]

Examples:

    $ env | jc --env -p
    [
      {
        "name": "XDG_SESSION_ID",
        "value": "1"
      },
      {
        "name": "HOSTNAME",
        "value": "localhost.localdomain"
      },
      {
        "name": "TERM",
        "value": "vt220"
      },
      {
        "name": "SHELL",
        "value": "/bin/bash"
      },
      {
        "name": "HISTSIZE",
        "value": "1000"
      },
      ...
    ]

    $ env | jc --env -p -r
    {
      "TERM": "xterm-256color",
      "SHELL": "/bin/bash",
      "USER": "root",
      "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
      "PWD": "/root",
      "LANG": "en_US.UTF-8",
      "HOME": "/root",
      "LOGNAME": "root",
      "_": "/usr/bin/env"
    }


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

    Dictionary of raw structured data or
    List of Dictionaries of processed structured data

## Parser Information
Compatibility:  linux, darwin, cygwin, win32, aix, freebsd

Version 1.3 by Kelly Brazil (kellyjonbrazil@gmail.com)
