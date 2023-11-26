"""
Napisz program, który sprawdzi czy dany klucz występuje już w słowniku.
"""

def check_if_key_already_in_dictionary(dict, key):
    if key in dict:
        print('This key has been used already.')
    else:
        print('This key hasn\'t been used yet.')

test_dict = {'key1':'value1',
             'key2':'value2'}

check_if_key_already_in_dictionary(test_dict, 'key2')
