"""
Wczytaj od użytkownika wartość klucza, następnie wypisz wartość przypisaną mu w
słowniku. W przypadku, gdy klucz nie istnieje powiadom o tym użytkownika.
"""

def print_value_by_key(dictionary, given_key):
    if given_key in dictionary:
        result = dictionary[given_key]
        print(result)
        return result
    else:
        print("Key not found")
        return "Key not found"

test_dict = {'a': -100, 'b': 2,'c': 50}
print_value_by_key(test_dict, 'b')
