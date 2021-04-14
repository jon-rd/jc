[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.cksum
jc - JSON CLI output utility `cksum` command output parser

This parser works with the following checksum calculation utilities:
- `sum`
- `cksum`

Usage (cli):

    $ cksum file.txt | jc --cksum

    or

    $ jc cksum file.txt

Usage (module):

    import jc.parsers.cksum
    result = jc.parsers.cksum.parse(cksum_command_output)

Schema:

    [
      {
        "filename":     string,
        "checksum":     integer,
        "blocks":       integer
      }
    ]

Examples:

    $ cksum * | jc --cksum -p
    [
      {
        "filename": "__init__.py",
        "checksum": 4294967295,
        "blocks": 0
      },
      {
        "filename": "airport.py",
        "checksum": 2208551092,
        "blocks": 3745
      },
      {
        "filename": "airport_s.py",
        "checksum": 1113817598,
        "blocks": 4572
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
Compatibility:  linux, darwin, cygwin, aix, freebsd

Version 1.1 by Kelly Brazil (kellyjonbrazil@gmail.com)
