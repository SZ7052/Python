"""
Exercise 2: Write another program that prompts for a
list of numbers as above and at the end prints out both the
maximum and minimum of the numbers instead of the average.

"""
Suma = 0
i = 0
caja=[]
largest = None
smallest = None

while True:
    entrada = input("Enter a number: ")

    if entrada == "done":
        break

    try:
        numero = int(entrada)
        if largest is None or numero > largest:
            largest = numero
        if smallest is None or numero < smallest:
            smallest = numero

        caja.append(numero)

    except ValueError:
        print("Invalid input")
        continue


if largest is not None and smallest is not None:
    print("largest: ", largest)
    print("smallest: ", smallest)
else:
    print("No numbers were entered")

