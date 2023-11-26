"""
Napisz program, który zsumuje wszystkie wartości ze słownika.
"""

def sum_dictionary_values(dictionary):
    sum = 0

    for key, value in dictionary.items():
        if isinstance(value, int):
            sum += value
    
    print(sum)
    return(sum)
    
test_dict = {'a': -100, 'b': 2,'c': 50}

sum_dictionary_values(test_dict)

