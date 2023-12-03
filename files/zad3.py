"""Odczytaj linia po linii 8 pierwszych linii tekstu, następnie wypisz je na ekran."""

try:
    with open('files/test.txt', 'r') as file:
        for _ in range(8):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("File not found.")