"""Odczytaj całą zawartość pliku i wypisz go na ekran."""

try:
    with open('files/test.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")