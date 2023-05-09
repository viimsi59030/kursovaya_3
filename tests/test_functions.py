import pytest

from main import a
from utils.func import load_bank_report, sort_operations, sort_operations_by_time, format_date, hide_card_numbers


def test_list():
    data = load_bank_report(a)
    assert isinstance(data, list)


def test_sort_operations(test_data):
    assert sort_operations(test_data[:2]) == [{
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58", "currency": {
                "name": "руб.", "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


def test_sort_operations_by_time(test_data):
    expected_result = [{"state": "EXECUTED",
                        "date": "2019-08-26T10:50:58.294041",
                        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}
                        },
                        "description": "Перевод организации", "from": "Maestro 1596837868705199",
                        "to": "Счет 64686473678894779589"},
                       {"date": "2019-07-03T18:35:29.512364",
                       "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}
                        },
                        "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                        "to": "Счет 35383033474447895560"},
                       {"date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}
                                            },
                        "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188"},
                       {"state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}
                                            },
                        "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
                        "to": "Счет 74489636417521191160"},
                       {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
                                            },
                        "description": "Перевод организации", "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702"}]
    assert sort_operations_by_time(test_data) == expected_result


def test_format_date(test_data):
    data = format_date(test_data)
    assert [i["date"] for i in data] == ["26.08.2019"]


# [{"state": "EXECUTED", "date": "26.08.2019",
#              "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}
#              }, "description": "Перевод организации", "from": "Maestro 1596837868705199",
#              "to": "Счет 64686473678894779589"}]


def test_hide_card_numbers(test_data):
    data = hide_card_numbers(test_data)
    assert data == ['1596 83** ****5, **9589']
