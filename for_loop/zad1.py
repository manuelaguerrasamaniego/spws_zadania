"""
Napisz program, który wczytuje od użytkownika kolejne wartości liczb całkowitych do momentu,
gdy ten poda wartość 0. Program wypisze wówczas na ekran komunikat ile użytkownik podał liczb
parzystych, a ile nieparzystych.
"""

def stop_at_zero():
    even_counter = 0
    odd_counter = 0

    while True:
        try:
            user_input = int(input("Enter an integer (0 to stop): "))

            if user_input == 0:
                break

            if user_input%2 == 0:
                even_counter+=1
            else:
                odd_counter+=1
        except ValueError:
            print("This is not an integer. Please enter an integer.")

    print(f"You entered {odd_counter} odd integers")
    print(f"You entered {even_counter} even integers")

stop_at_zero()            


