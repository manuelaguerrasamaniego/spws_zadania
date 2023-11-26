"""
Wypisz na ekran 30 pierwszych liczb ciągu fibonacciego: 0,1,1,2,3,5,8,13…
"""

def fibonacci_sequence(n):
    root = [0,1]

    while len(root) < n:
        root.append(root[-1] + root[-2])

    return root

print(fibonacci_sequence(30))


#druga opcja z pentlą for:

def fibonacci_sequence2(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=", ")
        a, b = b, (a + b)
    return ''

print(fibonacci_sequence2(30))