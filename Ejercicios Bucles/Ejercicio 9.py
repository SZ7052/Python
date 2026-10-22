"""
Ejercicio 9: Análisis de notas de alumnos
Crea un programa que dada una lista de las notas de un grupo de alumnos, calcule:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.
"""

notas = [4.5, 7.0, 9.2, 3.8, 5.0, 8.5, 2.0, 6.4]

aprobados = 0
suma_total = 0


nota_max = notas[0]
nota_min = notas[0]


for nota in notas:

    if nota >= 5.0:
        aprobados += 1


    suma_total += nota


    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota


media = suma_total / len(notas)



print(f"1. Alumnos aprobados: {aprobados}")
print(f"2. Nota media del grupo: {media:.2f}")
print(f"3. Nota más alta: {nota_max} | Nota más baja: {nota_min}")