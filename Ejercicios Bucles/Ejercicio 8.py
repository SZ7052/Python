"""
Ejercicio 8: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido.
"""
es_valido = False
n = 0


while not es_valido:
    try:
        n = int(input("Introduce un número mayor o igual a 2: "))
        if n >= 2:
            es_valido = True
        else:
            print("El número debe ser mayor o igual a 2.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

print(f"\nNúmeros primos entre 2 y {n}:")


for num in range(2, n + 1):
    es_primo = True
    divisor = 2


    while divisor < num and es_primo:
        if num % divisor == 0:
            es_primo = False
        divisor += 1

    if es_primo:
        print(num, end=" ")

