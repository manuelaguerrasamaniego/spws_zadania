"""
Napisz program, który znajdzie największą wartość całkowitą w słowniku.
"""

def find_max_int_value(dictionary):
    max_value = None

    for key, value in dictionary.items():
        if isinstance(value, int):
            if max_value is None or value > max_value:
                max_value = value

    if max_value is not None:
        print(max_value)
        return max_value
    else:
        print("No valid value found")
        return None
    
test_dict = {'a': -100, 'b': 2,'c': 50}

find_max_int_value(test_dict)