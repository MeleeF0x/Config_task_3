import json
import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_path", type=str, help="Path to the input TOML file")
    return parser.parse_args()

def read_input_file(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        return file.read()

def remove_comments(input_data):
    return re.sub(r'\(comment\s.*?\)', '', input_data, flags=re.DOTALL)

def parse_toml(input_data):
    constants = {}
    output_dict = {}
    for match in re.findall(r'([^\n]+)\s*->\s*([_a-zA-Z][_a-zA-Z0-9]*)', input_data):
        value, name = match
        value = value.strip()
        if value.isdigit():
            constants[name] = int(value)
        else:
            constants[name] = value
    dict_matches = re.findall(r'\{\s*(.*?)\s*\}', input_data, flags=re.DOTALL)
    for dict_content in dict_matches:
        entries = dict_content.split(';')
        dict_obj = {}
        for entry in entries:
            if not entry.strip():
                continue
            name, value = map(str.strip, entry.split('=', 1))
            if value.startswith('[') and value.endswith(']'):
                value = constants.get(value[1:-1], None)
            elif value.isdigit():
                value = int(value)
            dict_obj[name] = value
        output_dict.update(dict_obj)

    return output_dict

def format_output(output_dict):
    result = []
    for key, value in output_dict.items():
        if isinstance(value, int):
            result.append(f"{key} = {value};")
        elif isinstance(value, dict):
            nested = "; ".join(f"{k} = {v}" for k, v in value.items())
            result.append(f"{key} = {{ {nested} }};")
        else:
            result.append(f"{key} = \"{value}\";")
    return "\n".join(result)

def main():
    args = parse_args()
    try:
        input_data = read_input_file(args.input_file_path)
        input_data = remove_comments(input_data)

        parsed_data = parse_toml(input_data)
        output_text = format_output(parsed_data)

        print(output_text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
