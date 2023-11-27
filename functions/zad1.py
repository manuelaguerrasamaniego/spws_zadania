"""
Napisz program, który prosi o podanie liczby naturalnej, a następnie wypisuje z ilu cyfr składa się
wpisana wartość, a także informację o sumie tworzących ją cyfr. Dla uproszczenia załóż, że podana
liczba jest poprawna (czyli rzeczywiście naturalna).
"""

def natural_number():
    while True:
        num_str = input("Enter a natural number: ")

        try:
            num = int(num_str)    
            if num <= 0:
                print("Enter a valid natural number! ")
                continue
            else:
                break
        except ValueError:
            print("This is not a natural number. Enter a valid natural number! ")
    
    num_str = str(num)

    number_of_digits = len(num_str)
    digit_sum = sum(int(digit) for digit in num_str)

    print(f'This number is made out of {number_of_digits} digits.')
    print(f'The sum of the digits that make out your number is: {digit_sum}')

natural_number()