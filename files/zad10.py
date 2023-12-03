"""Napisz program, który zmieni zawartość pliku usuwając z niego przejścia do nowej linii."""
try:
    with open('files/test.txt', 'r') as file:
        content = file.read()

    content_without_newline_chars = content.replace('\n', '')

    print("Newline characters have been deleted succesfully.")

except FileNotFoundError:
    print("File not found.")
