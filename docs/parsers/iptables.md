[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.iptables
jc - JSON CLI output utility `ipables` command output parser

Supports `-vLn` and `--line-numbers` for all tables.

Usage (cli):

    $ sudo iptables -L -t nat | jc --iptables

    or

    $ jc iptables -L -t nat

Usage (module):

    import jc.parsers.iptables
    result = jc.parsers.iptables.parse(iptables_command_output)

Schema:

    [
      {
        "chain":                string,
        "rules": [
          {
            "num"               integer,
            "pkts":             integer,
            "bytes":            integer,  # converted based on suffix
            "target":           string,
            "prot":             string,
            "opt":              string,   # "--" = Null
            "in":               string,
            "out":              string,
            "source":           string,
            "destination":      string,
            "options":          string
          }
        ]
      }
    ]

Examples:

    $ sudo iptables --line-numbers -v -L -t nat | jc --iptables -p
    [
      {
        "chain": "PREROUTING",
        "rules": [
          {
            "num": 1,
            "pkts": 2183,
            "bytes": 186000,
            "target": "PREROUTING_direct",
            "prot": "all",
            "opt": null,
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": 2,
            "pkts": 2183,
            "bytes": 186000,
            "target": "PREROUTING_ZONES_SOURCE",
            "prot": "all",
            "opt": null,
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": 3,
            "pkts": 2183,
            "bytes": 186000,
            "target": "PREROUTING_ZONES",
            "prot": "all",
            "opt": null,
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": 4,
            "pkts": 0,
            "bytes": 0,
            "target": "DOCKER",
            "prot": "all",
            "opt": null,
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere",
            "options": "ADDRTYPE match dst-type LOCAL"
          }
        ]
      },
      ...
    ]

    $ sudo iptables --line-numbers -v -L -t nat | jc --iptables -p -r
    [
      {
        "chain": "PREROUTING",
        "rules": [
          {
            "num": "1",
            "pkts": "2183",
            "bytes": "186K",
            "target": "PREROUTING_direct",
            "prot": "all",
            "opt": "--",
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": "2",
            "pkts": "2183",
            "bytes": "186K",
            "target": "PREROUTING_ZONES_SOURCE",
            "prot": "all",
            "opt": "--",
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": "3",
            "pkts": "2183",
            "bytes": "186K",
            "target": "PREROUTING_ZONES",
            "prot": "all",
            "opt": "--",
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere"
          },
          {
            "num": "4",
            "pkts": "0",
            "bytes": "0",
            "target": "DOCKER",
            "prot": "all",
            "opt": "--",
            "in": "any",
            "out": "any",
            "source": "anywhere",
            "destination": "anywhere",
            "options": "ADDRTYPE match dst-type LOCAL"
          }
        ]
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
Compatibility:  linux

Version 1.5 by Kelly Brazil (kellyjonbrazil@gmail.com)
