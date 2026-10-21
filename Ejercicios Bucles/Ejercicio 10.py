"""
Ejercicio 10: Calcula inversión
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.
"""
es_valido = False


while not es_valido:
    try:
        inversion = float(input("Introduce la cantidad a invertir (€): "))
        interes = float(input("Introduce el interés anual (%): "))
        anios = int(input("Introduce el número de años: "))

        if inversion > 0 and interes > 0 and anios > 0:
            es_valido = True
        else:
            print("Todos los valores deben ser mayores que cero. Inténtalo de nuevo.\n")
    except ValueError:
        print("Error: Introduce números válidos (usando punto para decimales).\n")

capital = inversion

print(f"\nEvolución de la inversión de {inversion:.2f} € al {interes}% durante {anios} años:")


for anio in range(1, anios + 1):
    capital += capital * (interes / 100)
    print(f"Año {anio}: {capital:.2f} €")