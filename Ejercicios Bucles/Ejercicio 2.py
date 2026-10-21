print("=== TABLA DE MULTIPLICAR ===")
try:
    numero = int(input("Introduce un número entero: "))
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("❌ Error: Debes introducir un número entero válido.")
"""
Ejercicio 2: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
error usando try-except.
"""