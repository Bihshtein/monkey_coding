def print_json(json_object):
    print_value = '{'
    for index, (key, value) in enumerate(json_object.items()):
        print_value = append_item(print_value, key)
        print_value += ': '
        if isinstance(value, dict):
            print_value += print_json(value)
        elif isinstance(value, list):
            print_value += '['
            for i in range(len(value)):

                print_value += print_json(value[i])
                if i < len(value) -1:
                    print_value += ', '
            print_value += ']'
        else:
            print_value = append_item(print_value, value)
        if index < len(json_object) -1:
            print_value += ', '
    print_value += '}'
    return print_value


def append_item(print_value, item):
    if isinstance(item, str):
        return print_value + f'"{item}"'
    elif item is None :
        return print_value + 'null'
    else :
        return print_value + f'{item}'


import  unittest
import json

class Tests(unittest.TestCase):
    def test_simple_dict(self):
        json_obj = {"amount" : "50.00", "currency": "USD"}
        self.assertEqual(json.dumps(json_obj), print_json(json_obj), )

    def test_dict_in_dict(self):
        json_obj = {'taxes': {'T1': {'amount': '20.00', 'currency': 'USD'},
                  'T2': {'amount': '30.00', 'currency': 'USD'},
                  'T3': {'amount': '50.00', 'currency': 'USD'}}}
        expected = json.dumps(json_obj)
        self.assertEqual(expected, print_json(json_obj))

    def test_dict_list(self):
        json_obj = {'passengers': [{'first_name': 'JOHN', 'last_name': 'DOE', 'age': 18}, {'first_name': 'alex', 'last_name': 'DOE', 'age': 18}]}
        self.assertEqual(json.dumps(json_obj), print_json(json_obj))

    def test_full_obj(self):
        obj = {'reservation': {'passengers': [{'first_name': 'JOHN', 'last_name': 'DOE', 'age': 18}], 'flights': [
            {'origin': None, 'destination': 'New York', 'flight_number': 725, 'depart_at': '2021-02-15T15:00'},
            {'origin': 'New York', 'destination': 'Tel-Aviv', 'flight_number': 726, 'depart_at': '2021-02-25T07:00'}],
                               'price': {'total': {'amount': '700.00', 'currency': 'USD'},
                                         'base': {'amount': '600.00', 'currency': 'USD'},
                                         'taxes': {'T1': {'amount': '20.00', 'currency': 'USD'},
                                                   'T2': {'amount': '30.00', 'currency': 'USD'},
                                                   'T3': {'amount': '50.00', 'currency': 'USD'}}}}}
        self.assertEqual(json.dumps(obj), print_json(obj))