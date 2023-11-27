"""
Napisz funkcję wyliczającą pole prostokąta, przyjmując od użytkownika dwie dane o długości
boków.
"""

def rectangle_area():
    while True:
        a = input("Enter the length of side a in cm: ")
        b = input("Enter the length of side b in cm: ")

        try:
            a_int = int(a)
            b_int = int(b)
            area = a_int * b_int
            print(f"The area is: {area} cm squared")
            return area
        except ValueError:
            print("Enter valid values!")
        
rectangle_area()