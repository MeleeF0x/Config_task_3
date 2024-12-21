import unittest
from io import StringIO
import sys

# Импортируем функции из основного кода
from main import remove_comments, parse_toml, format_output

class TestConfigParser(unittest.TestCase):

    def test_parse_toml_simple(self):
        input_data = '''
        value1 -> constant1
        value2 -> constant2

        { key1 = value1; key2 = 123; key3 = [constant1]; }
        '''
        expected = {
            'key1': 'value1',
            'key2': 123,
            'key3': 'value1',
        }

        result = parse_toml(input_data)
        self.assertEqual(result, expected)

    def test_remove_comments(self):
        input_data = '''
        (comment
        This is a comment
        that spans multiple
        lines
        )

        value1 -> constant1

        { key1 = value1; }
        '''
        expected = '''
        

        value1 -> constant1

        { key1 = value1; }
        '''

        result = remove_comments(input_data)
        self.assertEqual(result, expected)

    def test_format_output(self):
        output_dict = {
            'key1': 'value1',
            'key2': 123,
            'key3': 'value2',
            'nested_dict': {'keyA': 'nested value', 'keyB': 456}
        }

        expected = '''key1 = "value1";
key2 = 123;
key3 = "value2";
nested_dict = { keyA = nested value; keyB = 456 };'''

        result = format_output(output_dict)
        self.assertEqual(result, expected)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()