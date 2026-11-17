"""
Exercise 1: Write a program which repeatedly reads integers
until the user enters “done”. Once “done” is entered,
print out the total, count, and average of the integers.
If the user enters anything other than an integer,
detect their mistake using try and except and print
an error message and skip to the next integers.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""

Suma = 0
i = 0

while True:
    entrada = input("Enter a number: ")

    if entrada == "done":
        break

    try:
        numero = int(entrada)
        Suma += numero
        i += 1
    except ValueError:
        print("Invalid input")
        continue

if i > 0:
    Media = Suma / i
    print(Suma, i, Media)
else:
    print("No numbers were entered")