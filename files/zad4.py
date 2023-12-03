"""Dopisz do pliku dodatkową linię tekstu z informacją o autorze dzieła."""

try:
    with open('files/test.txt', 'a') as file:
        file.write("\nAuthor: Bjork\n")
    
    with open('files/test.txt', 'r') as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")