import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f_handler:
        return json.load(f_handler)


def pretty_json_formatter(parsed_json_data):
    return json.dumps(parsed_json_data,
                      indent=4,
                      sort_keys=True,
                      ensure_ascii=False)


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    print(pretty_json_formatter(parsed_json))

