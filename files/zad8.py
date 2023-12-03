"""Napisz program, który skopiuje zawartość pliku test.txt do pliku test_kopia.txt."""

try:
    with open('files/test.txt', 'r') as source_file:
        content = source_file.read()

    with open('files/test_kopia.txt', 'w') as destination_file:
        destination_file.write(content)
    
    print("A copy has been made.")

except FileNotFoundError:
    print("File not found.")
