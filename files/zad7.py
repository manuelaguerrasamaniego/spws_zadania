"""Napisz program, który wypisze na ekran ilość znaków w pliku. Nie do końca rozumiem czy mają w tym być spacje? Zrobiłam tak i tak."""

try:
    with open('files/test.txt', 'r') as file:
        content = file.read()

    content_without_spaces = content.replace(" ", "")

    character_count_no_spaces = len(content_without_spaces)
    character_count_with_spaces = len(content)

    print(f"The number of characters with spaces is: {character_count_with_spaces}")
    print(f"The number of characters without spaces is: {character_count_no_spaces}")

except FileNotFoundError:
    print("File not found.")