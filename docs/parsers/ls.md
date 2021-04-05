
# jc.parsers.ls
jc - JSON CLI output utility `ls` and `vdir` command output parser

Options supported:
- `lbaR1`
- `--time-style=full-iso`
- `-h`: File sizes will be available in text form with `-r` but larger file sizes with human readable suffixes will be converted to `Null` in the default view since the parser attempts to convert this field to an integer.

Note: The `-1`, `-l`, or `-b` option of `ls` should be used to correctly parse filenames that include newline characters. Since `ls` does not encode newlines in filenames when outputting to a pipe it will cause `jc` to see multiple files instead of a single file if `-1`, `-l`, or `-b` is not used. Alternatively, `vdir` can be used, which is the same as running `ls -lb`.

The `epoch` calculated timestamp field is naive (i.e. based on the local time of the system the parser is run on)

The `epoch_utc` calculated timestamp field is timezone-aware and is only available if the timezone field is UTC.

Usage (cli):

    $ ls | jc --ls

    or

    $ jc ls

Usage (module):

    import jc.parsers.ls
    result = jc.parsers.ls.parse(ls_command_output)

Compatibility:

    'linux', 'darwin', 'cygwin', 'aix', 'freebsd'

Examples:

    $ ls /usr/bin | jc --ls -p
    [
      {
        "filename": "apropos"
      },
      {
        "filename": "arch"
      },
      {
        "filename": "awk"
      },
      {
        "filename": "base64"
      },
      ...
    ]

    $ ls -l /usr/bin | jc --ls -p
    [
      {
        "filename": "apropos",
        "link_to": "whatis",
        "flags": "lrwxrwxrwx.",
        "links": 1,
        "owner": "root",
        "group": "root",
        "size": 6,
        "date": "Aug 15 10:53"
      },
      {
        "filename": "ar",
        "flags": "-rwxr-xr-x.",
        "links": 1,
        "owner": "root",
        "group": "root",
        "size": 62744,
        "date": "Aug 8 16:14"
      },
      {
        "filename": "arch",
        "flags": "-rwxr-xr-x.",
        "links": 1,
        "owner": "root",
        "group": "root",
        "size": 33080,
        "date": "Aug 19 23:25"
      },
      ...
    ]

    $ ls -l /usr/bin | jc --ls -p -r
    [
      {
        "filename": "apropos",
        "link_to": "whatis",
        "flags": "lrwxrwxrwx.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "6",
        "date": "Aug 15 10:53"
      },
      {
        "filename": "arch",
        "flags": "-rwxr-xr-x.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "33080",
        "date": "Aug 19 23:25"
      },
      {
        "filename": "awk",
        "link_to": "gawk",
        "flags": "lrwxrwxrwx.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "4",
        "date": "Aug 15 10:53"
      },
      {
        "filename": "base64",
        "flags": "-rwxr-xr-x.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "37360",
        "date": "Aug 19 23:25"
      },
      {
        "filename": "basename",
        "flags": "-rwxr-xr-x.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "29032",
        "date": "Aug 19 23:25"
      },
      {
        "filename": "bash",
        "flags": "-rwxr-xr-x.",
        "links": "1",
        "owner": "root",
        "group": "root",
        "size": "964600",
        "date": "Aug 8 05:06"
      },
      ...
    ]

    $ ls -l /usr/bin | jc --ls | jq '.[] | select(.size > 50000000)'
    {
      "filename": "emacs",
      "flags": "-r-xr-xr-x",
      "links": 1,
      "owner": "root",
      "group": "wheel",
      "size": 117164432,
      "date": "May 3 2019"
    }


## info
```python
info()
```


## process
```python
process(proc_data)
```

Final processing to conform to the schema.

Parameters:

    proc_data:   (List of Dictionaries) raw structured data to process

Returns:

    List of Dictionaries. Structured data with the following schema:

    [
      {
        "filename":     string,
        "flags":        string,
        "links":        integer,
        "parent":       string,
        "owner":        string,
        "group":        string,
        "size":         integer,
        "date":         string,
        "epoch":        integer,     # naive timestamp if date field exists and can be converted
        "epoch_utc":    integer      # timezone aware timestamp if date field is in UTC and can be converted
      }
    ]


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

