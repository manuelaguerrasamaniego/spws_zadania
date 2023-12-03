"""Wczytaj zawartość pliku linia po linii, następnie umieść je w zmiennej. Wypisz zawartość na ekran."""

try:
    with open('files/test.txt','r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print("File not found.")