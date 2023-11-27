"""
Napisz funkcję, która przyjmuje wartość temperatury w Kelvinach i zwraca wartość wyrażoną w
stopniach Celsjusza: TC = TK − 272.15. W przypadku podania wartości ujemnej funkcja zwraca
None.
"""

def kelvin_to_celcius():
    while True:
        kelvin = input("Enter your temperature in Kelvins: ")

        try:
            if float(kelvin) < 0:
                return None
            else:
                celcius = float(kelvin) - 272.15
                print(f"{kelvin} in Kelvins is {celcius} in Celcius")
                return celcius
        except ValueError:
            print("Enter a valid temperature!")

kelvin_to_celcius()