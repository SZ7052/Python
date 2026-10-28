 # // Ejercicio 5. Números repetidos
 # // Dispones de dos listas de números enteros.
 # // Utiliza dos bucles for anidados para encontrar los números que aparecen en ambas listas y
 # // mostrarlos por pantalla.
 # // Cada número común deberá mostrarse una sola vez.

nombres1=[1,2,3,4]
nombres2=[7,8,9,1]

for i in nombres1:
    for j in nombres2:
        if nombres1[i]==nombres2[j]:
            print(nombres1[i])
            print(nombres2[j])
