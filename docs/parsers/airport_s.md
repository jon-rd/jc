[Home](https://kellyjonbrazil.github.io/jc/)

# jc.parsers.airport_s
jc - JSON CLI output utility `airport -s` command output parser

The `airport` program can be found at `/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport`.

Usage (cli):

    $ airport -s | jc --airport-s

    or

    $ jc airport -s

Usage (module):

    import jc.parsers.airport_s
    result = jc.parsers.airport_s.parse(airport_s_command_output)

Schema:

    [
      {
        "ssid":         string,
        "bssid":        string,
        "rssi":         integer,
        "channel":      string,
        "ht":           boolean,
        "cc":           string,
        "security": [
                        string,
        ]
      }
    ]

Examples:

    $ airport -s | jc --airport-s -p
    [
      {
        "ssid": "DIRECT-4A-HP OfficeJet 3830",
        "bssid": "00:67:eb:2a:a7:3b",
        "rssi": -90,
        "channel": "6",
        "ht": true,
        "cc": "--",
        "security": [
          "WPA2(PSK/AES/AES)"
        ]
      },
      {
        "ssid": "Latitude38",
        "bssid": "c0:ff:d5:d2:7a:f3",
        "rssi": -85,
        "channel": "11",
        "ht": true,
        "cc": "US",
        "security": [
          "WPA2(PSK/AES/AES)"
        ]
      },
      {
        "ssid": "xfinitywifi",
        "bssid": "6e:e3:0e:b8:45:99",
        "rssi": -83,
        "channel": "11",
        "ht": true,
        "cc": "US",
        "security": [
          "NONE"
        ]
      },
      ...
    ]

    $ airport -s | jc --airport -p -r
    [
      {
        "ssid": "DIRECT-F3-HP ENVY 5660 series",
        "bssid": "b0:5a:da:6f:0a:d4",
        "rssi": "-93",
        "channel": "1",
        "ht": "Y",
        "cc": "--",
        "security": "WPA2(PSK/AES/AES)"
      },
      {
        "ssid": "YouAreInfected-5",
        "bssid": "5c:e3:0e:c2:85:da",
        "rssi": "-85",
        "channel": "36",
        "ht": "Y",
        "cc": "US",
        "security": "WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)"
      },
      {
        "ssid": "YuanFamily",
        "bssid": "5c:e3:0e:b8:5f:9a",
        "rssi": "-84",
        "channel": "11",
        "ht": "Y",
        "cc": "US",
        "security": "WPA(PSK/AES,TKIP/TKIP) WPA2(PSK/AES,TKIP/TKIP)"
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
Compatibility:  darwin

Version 1.3 by Kelly Brazil (kellyjonbrazil@gmail.com)
