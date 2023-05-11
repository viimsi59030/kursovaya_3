import json
import os.path
from datetime import datetime

a = os.path.join('../utils/operations.json')


def load_bank_report(filename):
    """Загружаем данные по операциям из json"""

    with open(filename, 'r', encoding='utf-8') as file:
        bank_data = json.load(file)
        return bank_data


def sort_operations(exe_operations):
    """Формируем список с учетом выполненных операций"""

    list_operations = []
    for i in exe_operations:
        if all(key in i and i[key] for key in
               ["state", "date", "description", "from", "to", "operationAmount"]):
            if i.get("state") == "EXECUTED":
                list_operations.append(i)
    return list_operations


def sort_operations_by_time(list_operations):
    """Сортирую список выполненных операций по дате и вывожу последние 5"""

    sorted_data = sorted(list_operations, key=lambda x: x['date'], reverse=True)
    return sorted_data[:5]


def format_date(date):
    """Преобразую дату из одного формата в требуемый согласно ТЗ заказчика"""

    date_new = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date_new

def hide_card_numbers(operations):
    """Скрываем часть номера карты и счета за звездочками"""

    number = operations.split()[-1]
    name = operations.split()[0]
    if len(number) == 16:
        card_number = name[:] + " " + number[:4] + " " + number[4:6] + "** ****" + number[-4]
        return card_number

    else:
        card_number = name[:] + " " + "**" + number[-4:]
        return card_number
