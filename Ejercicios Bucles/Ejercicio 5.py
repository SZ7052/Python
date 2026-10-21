print("=== NÚMEROS REPETIDOS EN DOS LISTAS ===")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

comunes = []
for n1 in lista1:
    for n2 in lista2:
        if n1 == n2 and n1 not in comunes:
            comunes.append(n1)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Números comunes (sin repetir): {comunes}")
"""
Ejercicio 5. Números repetidos
Dispones de dos listas de números enteros.
Utiliza dos bucles for anidados para encontrar los números que aparecen en ambas listas y
mostrarlos por pantalla.
Cada número común deberá mostrarse una sola vez
"""