[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.jobs
jc - JSON CLI output utility `jobs` command output parser

Also supports the `-l` option.

Usage (cli):

    $ jobs | jc --jobs

    or

    $ jc jobs

Usage (module):

    import jc.parsers.jobs
    result = jc.parsers.jobs.parse(jobs_command_output)

Schema:

    [
      {
        "job_number":   integer,
        "pid":          integer,
        "history":      string,
        "status":       string,
        "command":      string
      }
    ]

Example:

    $ jobs -l | jc --jobs -p
    [
      {
        "job_number": 1,
        "pid": 5283,
        "status": "Running",
        "command": "sleep 10000 &"
      },
      {
        "job_number": 2,
        "pid": 5284,
        "status": "Running",
        "command": "sleep 10100 &"
      },
      {
        "job_number": 3,
        "pid": 5285,
        "history": "previous",
        "status": "Running",
        "command": "sleep 10001 &"
      },
      {
        "job_number": 4,
        "pid": 5286,
        "history": "current",
        "status": "Running",
        "command": "sleep 10112 &"
      }
    ]

    $ jobs -l | jc --jobs -p -r
    [
      {
        "job_number": "1",
        "pid": "19510",
        "status": "Running",
        "command": "sleep 1000 &"
      },
      {
        "job_number": "2",
        "pid": "19511",
        "status": "Running",
        "command": "sleep 1001 &"
      },
      {
        "job_number": "3",
        "pid": "19512",
        "history": "previous",
        "status": "Running",
        "command": "sleep 1002 &"
      },
      {
        "job_number": "4",
        "pid": "19513",
        "history": "current",
        "status": "Running",
        "command": "sleep 1003 &"
      }
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

Version 1.3 by Kelly Brazil (kellyjonbrazil@gmail.com)
