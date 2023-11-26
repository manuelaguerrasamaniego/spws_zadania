"""
Wypisz na ekran liczby z przedziału <0,10>, które nie zawierają w sobie cyfr 3 oraz 6.
"""

for num in range(11):
    if num not in [3, 6]:
        print(num)
