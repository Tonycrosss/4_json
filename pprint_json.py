import json


def load_data(filepath, encoding_type):
    with open(filepath, 'r', encoding='{}'.format(encoding_type)) as f_handler:
        return json.load(f_handler)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


if __name__ == '__main__':
    filepath = input('Введите полный путь до файла json\n')
    encoding_type = input('Введите название кодировки файла (utf-8 и т.д)\n')
    parsed_json = load_data(filepath, encoding_type)
    print(pretty_print_json(parsed_json))