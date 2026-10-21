"""
Ejercicio 7: Entradas de cine
Un cine cobra las entradas a distinto precio en función de la edad del espectador. Los
menores de 3 años entran gratis, los niños de entre 3 y 12 años pagan 8 € y la entradas
para mayores de 12 años cuesta 12 €.
● Calcula y muestra el precio de la entrada para 6 usuarios.
● Calcula y muestra el precio de la entrada hasta que el usuario introduzca un
valor negativo
"""


#1

for i in range(6):
    try:
        edad = int(input(f"Introduce la edad del usuario {i + 1}: "))

        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad < 3:
            print("El precio es: GRATIS (0 €)")
        elif edad <= 12:
            print("El precio es: 8 €")
        else:
            print("El precio es: 12 €")
    except ValueError:
        print("Error: Introduce un número entero válido.")



#2


continuar = True
while continuar:
    try:
        edad = int(input("Introduce la edad del espectador (número negativo para salir): "))

        if edad < 0:
            print("Saliendo")
            continuar = False
        elif edad < 3:
            print("El precio es: GRATIS")
        elif edad <= 12:
            print("El precio es: 8 €")
        else:
            print("El precio es: 12 €")
    except ValueError:
        print("Error: Introduce un número entero válido.")