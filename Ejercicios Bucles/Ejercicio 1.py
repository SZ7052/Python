print("=== CALCULADORA BÁSICA ===")
while True:
    print("\nOperaciones disponibles: +, -, *, /")
    print("Escribe 'salir' para terminar.")

    op = input("Introduce la operación (+, -, *, /) o 'salir': ").strip().lower()
    if op == 'salir':
        print("¡Hasta luego!")
        break

    if op not in ('+', '-', '*', '/'):
        print("❌ Operación no válida. Inténtalo de nuevo.")
        continue

    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("❌ Error: Debes introducir un valor numérico válido.")
        continue

    if op == '+':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif op == '-':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif op == '*':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif op == '/':
        if num2 == 0:
            print("❌ Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
"""
Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división
por cero y entrada de datos no numéricos.
"""
while True:

    print("Suma")
    print("Resta")
    print("Multiplicacion")
    print("Divicion")
    print("Salir")

    line = input('>').strip()

    if line == 'Salir':
        break

    if line in ('Suma', 'Resta', 'Multiplicacion', 'Division'):
        n1=int(input('Dime n1: '))
        n2=int(input('Dime n2: '))

        if line == 'Suma':
            print('Resultado:', n1 + n2)
        elif line == 'Resta':
            print('Resultado:', n1 - n2)
        elif line == 'Multiplicacion':
            print('Resultado:', n1 * n2)
        elif line == 'Division':
            if n2 == 0:
                print('No se puede dividir entre 0')
            else:
                print('Resultado:', n1 / n2)
    else:
        print('Opción no válida')










