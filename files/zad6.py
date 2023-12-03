"""Napisz program, który odnajdzie najdłuższy wyraz w pliku."""
import string

try:
    with open('files/test.txt', 'r') as file:
        content = file.read()

    words = content.split()

    words = [word.strip(string.punctuation) for word in words]

    longest_word = max(words, key=len)

    print(f"The longest word in this file is: {longest_word}.")

except FileNotFoundError:
    print("File not found.")