"""Napisz program, który odczyta jedną, losową linię z pliku."""
import random

try:
    with open('files/test.txt', 'r') as file:
        lines = file.readlines()

    if lines:
        random_line = random.choice(lines)

        print("Random line:")
        print(random_line.strip())
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("File not found.")

