import unittest
import pygments
from pygments.token import (Name, Number, String, Keyword)
import jc.cli


class MyTests(unittest.TestCase):
    def test_cli_generate_magic_command(self):
        commands = {
            'jc -p systemctl list-sockets': 'systemctl list-sockets | jc --systemctl-ls -p',
            'jc -p systemctl list-unit-files': 'systemctl list-unit-files | jc --systemctl-luf -p',
            'jc -p pip list': 'pip list | jc --pip-list -p',
            'jc -p pip3 list': 'pip3 list | jc --pip-list -p',
            'jc -p pip show jc': 'pip show jc | jc --pip-show -p',
            'jc -p pip3 show jc': 'pip3 show jc | jc --pip-show -p',
            'jc -prd last': 'last | jc --last -prd',
            'jc -prd lastb': 'lastb | jc --last -prd',
            'jc -p airport -I': 'airport -I | jc --airport -p',
            'jc -p -r airport -I': 'airport -I | jc --airport -pr',
            'jc -prd airport -I': 'airport -I | jc --airport -prd',
            'jc -p nonexistent command': 'nonexistent command',
            'jc -ap': None,
            'jc -a arp -a': None,
            'jc -v': None,
            'jc -h': None,
            'jc -h --arp': None,
            'jc -h arp': None,
            'jc -h arp -a': None
        }

        for command, expected_command in commands.items():
            self.assertEqual(jc.cli.generate_magic_command(command.split(' '))[1], expected_command)

    def test_cli_set_env_colors(self):
        if pygments.__version__.startswith('2.3.'):
            env = {
                '': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                },
                ' ': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                },
                'default,default,default,default': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                },
                'red,red,red,red': {
                    Name.Tag: 'bold #ansidarkred',
                    Keyword: '#ansidarkred',
                    Number: '#ansidarkred',
                    String: '#ansidarkred'
                },
                'red,red,yada,red': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                },
                'red,red,red': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                },
                'red,red,red,red,red,red': {
                    Name.Tag: 'bold #ansidarkblue',
                    Keyword: '#ansidarkgray',
                    Number: '#ansipurple',
                    String: '#ansidarkgreen'
                }
            }
        else:
            env = {
                '': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                },
                ' ': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                },
                'default,default,default,default': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                },
                'red,red,red,red': {
                    Name.Tag: 'bold ansired',
                    Keyword: 'ansired',
                    Number: 'ansired',
                    String: 'ansired'
                },
                'red,red,yada,red': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                },
                'red,red,red': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                },
                'red,red,red,red,red,red': {
                    Name.Tag: 'bold ansiblue',
                    Keyword: 'ansibrightblack',
                    Number: 'ansimagenta',
                    String: 'ansigreen'
                }
            }

        for jc_colors, expected_colors in env.items():
            self.assertEqual(jc.cli.set_env_colors(jc_colors), expected_colors)

    def test_cli_json_out(self):
        test_input = [
            None,
            {},
            [],
            '',
            {"key1": "value1", "key2": 2, "key3": None, "key4": 3.14, "key5": True},
        ]

        if pygments.__version__.startswith('2.3.'):
            expected_output = [
                '\x1b[30;01mnull\x1b[39;00m',
                '{}',
                '[]',
                '\x1b[32m""\x1b[39m',
                '{\x1b[34;01m"key1"\x1b[39;00m:\x1b[32m"value1"\x1b[39m,\x1b[34;01m"key2"\x1b[39;00m:\x1b[35m2\x1b[39m,\x1b[34;01m"key3"\x1b[39;00m:\x1b[30;01mnull\x1b[39;00m,\x1b[34;01m"key4"\x1b[39;00m:\x1b[35m3.14\x1b[39m,\x1b[34;01m"key5"\x1b[39;00m:\x1b[30;01mtrue\x1b[39;00m}'
            ]
        else:
            expected_output = [
                '\x1b[90mnull\x1b[39m',
                '{}',
                '[]',
                '\x1b[32m""\x1b[39m',
                '{\x1b[34;01m"key1"\x1b[39;00m:\x1b[32m"value1"\x1b[39m,\x1b[34;01m"key2"\x1b[39;00m:\x1b[35m2\x1b[39m,\x1b[34;01m"key3"\x1b[39;00m:\x1b[90mnull\x1b[39m,\x1b[34;01m"key4"\x1b[39;00m:\x1b[35m3.14\x1b[39m,\x1b[34;01m"key5"\x1b[39;00m:\x1b[90mtrue\x1b[39m}'
            ]

        for test_dict, expected_json in zip(test_input, expected_output):
            self.assertEqual(jc.cli.json_out(test_dict), expected_json)

    def test_cli_json_out_mono(self):
        test_input = [
            None,
            {},
            [],
            '',
            {"key1": "value1", "key2": 2, "key3": None, "key4": 3.14, "key5": True},
        ]

        expected_output = [
            'null',
            '{}',
            '[]',
            '""',
            '{"key1":"value1","key2":2,"key3":null,"key4":3.14,"key5":true}'
        ]

        for test_dict, expected_json in zip(test_input, expected_output):
            self.assertEqual(jc.cli.json_out(test_dict, mono=True), expected_json)

    def test_cli_json_out_pretty(self):
        test_input = [
            {"key1": "value1", "key2": 2, "key3": None, "key4": 3.14, "key5": True},
            {"key1": [{"subkey1": "subvalue1"}, {"subkey2": [1, 2, 3]}], "key2": True}
        ]

        if pygments.__version__.startswith('2.3.'):
            expected_output = [
                '{\n  \x1b[34;01m"key1"\x1b[39;00m: \x1b[32m"value1"\x1b[39m,\n  \x1b[34;01m"key2"\x1b[39;00m: \x1b[35m2\x1b[39m,\n  \x1b[34;01m"key3"\x1b[39;00m: \x1b[30;01mnull\x1b[39;00m,\n  \x1b[34;01m"key4"\x1b[39;00m: \x1b[35m3.14\x1b[39m,\n  \x1b[34;01m"key5"\x1b[39;00m: \x1b[30;01mtrue\x1b[39;00m\n}',
                '{\n  \x1b[34;01m"key1"\x1b[39;00m: [\n    {\n      \x1b[34;01m"subkey1"\x1b[39;00m: \x1b[32m"subvalue1"\x1b[39m\n    },\n    {\n      \x1b[34;01m"subkey2"\x1b[39;00m: [\n        \x1b[35m1\x1b[39m,\n        \x1b[35m2\x1b[39m,\n        \x1b[35m3\x1b[39m\n      ]\n    }\n  ],\n  \x1b[34;01m"key2"\x1b[39;00m: \x1b[30;01mtrue\x1b[39;00m\n}'
            ]
        else:
            expected_output = [
                '{\n  \x1b[34;01m"key1"\x1b[39;00m: \x1b[32m"value1"\x1b[39m,\n  \x1b[34;01m"key2"\x1b[39;00m: \x1b[35m2\x1b[39m,\n  \x1b[34;01m"key3"\x1b[39;00m: \x1b[90mnull\x1b[39m,\n  \x1b[34;01m"key4"\x1b[39;00m: \x1b[35m3.14\x1b[39m,\n  \x1b[34;01m"key5"\x1b[39;00m: \x1b[90mtrue\x1b[39m\n}',
                '{\n  \x1b[34;01m"key1"\x1b[39;00m: [\n    {\n      \x1b[34;01m"subkey1"\x1b[39;00m: \x1b[32m"subvalue1"\x1b[39m\n    },\n    {\n      \x1b[34;01m"subkey2"\x1b[39;00m: [\n        \x1b[35m1\x1b[39m,\n        \x1b[35m2\x1b[39m,\n        \x1b[35m3\x1b[39m\n      ]\n    }\n  ],\n  \x1b[34;01m"key2"\x1b[39;00m: \x1b[90mtrue\x1b[39m\n}'
            ]

        for test_dict, expected_json in zip(test_input, expected_output):
            self.assertEqual(jc.cli.json_out(test_dict, pretty=True), expected_json)

    def test_cli_about_jc(self):
        self.assertEqual(jc.cli.about_jc()['name'], 'jc')
        self.assertGreaterEqual(jc.cli.about_jc()['parser_count'], 55)
        self.assertEqual(jc.cli.about_jc()['parser_count'], len(jc.cli.about_jc()['parsers']))
