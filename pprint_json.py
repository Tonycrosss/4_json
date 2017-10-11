import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


if __name__ == '__main__':
    filepath = input('Введите полный путь до файла json\n')
    parsed_json = load_data(filepath)
    print(pretty_print_json(parsed_json))