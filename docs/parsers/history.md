[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.history
jc - JSON CLI output utility `history` command output parser

This parser will output a list of dictionaries each containing `line` and `command` keys. If you would like a simple dictionary output, then use the `-r` command-line option or the `raw=True` argument in the `parse()` function.

Usage (cli):

    $ history | jc --history

Usage (module):

    import jc.parsers.history
    result = jc.parsers.history.parse(history_command_output)

Schema:

    [
      {
        "line":     integer,
        "command":  string
      }
    ]

Examples:

    $ history | jc --history -p
    [
      {
        "line": 118,
        "command": "sleep 100"
      },
      {
        "line": 119,
        "command": "ls /bin"
      },
      {
        "line": 120,
        "command": "echo "hello""
      },
      {
        "line": 121,
        "command": "docker images"
      },
      ...
    ]

    $ history | jc --history -p -r
    {
      "118": "sleep 100",
      "119": "ls /bin",
      "120": "echo "hello"",
      "121": "docker images",
      ...
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
Compatibility:  linux, darwin, cygwin, aix, freebsd

Version 1.4 by Kelly Brazil (kellyjonbrazil@gmail.com)
