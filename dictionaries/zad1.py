"""
Napisz program, który doda nowy element do istniejącego słownika.
"""

def add_element_to_dictionary(dictionary, key, value):
    dictionary.update({key: value})
    return dictionary



test_dict = {'klucz': 'wartosc',
             'klucz2': 'wartosc2'}

add_element_to_dictionary(test_dict, 'klucz3', 'wartosc3')
print(test_dict)