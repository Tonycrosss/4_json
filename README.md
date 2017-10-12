# Приятный JSON

Данный модуль включает в себя следующие функции:
* _load_data(filepath, encoding_type)_
Принимает путь до файла json и тип кодировки, а затем парсит этот файл

* _pretty_print_json(data)_
Принимает информацию после парсинга и выводит ее в Pretty Json на экран


# Использование


Пример запуска на Windows, Python 3.5:

```bash
$ python pprint_json.py
Введите полный путь до файла json
./alco_shops.json
Введите название кодировки файла (utf-8 и т.д)
utf-8-sig


```

После чего мы получим вывод в формате Pretty json:

```bash
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "\u0443\u043b\u0438\u0446\u0430 \u0410\u043a\u0430\u0434\u0435\u043c\u0438\u043a\u0430 \u041f\u0430\u0432\u043b\u043e\u0432\u0430, \u0434\u043e\u043c 10",
                    "AdmArea": "\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433",
                    "ClarificationOfWorkingHours": null,
                    "District": "\u0440\u0430\u0439\u043e\u043d \u041a\u0443\u043d\u0446\u0435\u0432\u043e",
                    "IsNetObject": "\u0434\u0430",
                    "Name": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
                    "OperatingCompany": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
                    "TypeService": "\u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "\u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a",
                            "Hours": "09:30-22:30"
                        }...........


```
# Цели проекта

Код написан исключительно в обучающих целях. Курс для обучения python - [DEVMAN.org](https://devman.org)
