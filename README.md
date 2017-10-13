# Приятный JSON

Данный модуль включает в себя следующие функции:
* _load_data(filepath)_  
Принимает путь до файла json, а затем парсит этот файл

* _pretty_print_json(data)_  
Принимает информацию после парсинга и выводит ее в Pretty Json на экран


# Использование


Пример запуска на Windows, Python 3.5:

```bash
$ python pprint_json.py путь_до_файла.json


```

После чего мы получим вывод в формате Pretty json:

```bash
{
    "glossary": {
        "GlossDiv": {
            "GlossList": {
                "GlossEntry": {
                    "Abbrev": "ISO 8879:1986",
                    "Acronym": "SGML",
                    "GlossDef": {
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ],
                        "para": "A meta-markup language, used to create markup languages such as DocBook."
                    },
                    "GlossSee": "markup",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "ID": "SGML",
                    "SortAs": "SGML"
                }
            },
            "title": "S"
        },
        "title": "example glossary"
    }
}


```
# Цели проекта

Код написан исключительно в обучающих целях. Курс для обучения python - [DEVMAN.org](https://devman.org)
