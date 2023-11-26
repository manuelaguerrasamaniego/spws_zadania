"""
Napisz program, który połączy zawartość trzech słowników w jeden.
"""

def merge_dicts(*args):
    new_dict = {}
    for dictionary in args:
        new_dict.update(dictionary)
    return new_dict


dict1 = {'key1': 'value1'}
dict2 = {'key2': 'value2'}
dict3 = {'key3': 'value3'}

test_dict = merge_dicts(dict1, dict2, dict3)
print(test_dict)
