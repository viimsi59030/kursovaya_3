from utils import func
import os.path

a = os.path.join('utils/operations.json')

first = func.load_bank_report(a)
second = func.sort_operations(first)
third = func.sort_operations_by_time(second)


def print_operation(data):
    for i in range(len(data)):
        print(f'{func.format_date(data[i]["date"])} {data[i]["description"]}\n' \
              f'{func.hide_card_numbers(data[i]["from"])} -> {func.hide_card_numbers(data[i]["to"])}\n' \
              f'{data[i]["operationAmount"]["amount"]} {data[i]["operationAmount"]["currency"]["name"]}\n')


print_operation(third)
