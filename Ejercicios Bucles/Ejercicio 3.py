"""
Ejercicio 3: Cuenta atrás
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla
la cuenta atrás desde ese número hasta cero separados por comas.
"""

num = int(input(">"))
try:

    while num>=0:
        if num>0:
            print(f"{num},", end=" ")
        else:
            print(num)

        num-=1



except ValueError:
    print("Error")