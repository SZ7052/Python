"""
Ejercicio 11: Múltiplos
Escribe un programa que busque el primer número múltiplo de 7 que también sea mayor
que 80 y menor que 200. El programa debe saltar los números que no son múltiplos de 7 y
detenerse al encontrar el primero
"""
encontrado = False

for numero in range(81, 200):

    if numero % 7 != 0:
        continue


    print(f"El primer múltiplo de 7 mayor que 80 y menor que 200 es: {numero}")
    encontrado = True
    break
if not encontrado:
    print("No se encontró ninguno.")