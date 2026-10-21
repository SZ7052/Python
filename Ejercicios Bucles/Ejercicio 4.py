print("=== COMBINACIONES DE MENÚ ===")
comidas = ["Hamburguesa", "Pizza", "Ensalada", "Pasta"]
bebidas = ["Agua", "Refresco", "Vino", "Zumo"]

contador = 1
for comida in comidas:
    for bebida in bebidas:
        print(f"Combinación {contador}: {comida} con {bebida}")
        contador += 1
"""
Ejercicio 4. Menús del restaurante
Un restaurante ofrece varias comidas y varias bebidas.
Utiliza dos bucles for anidados para mostrar todas las combinaciones posibles de comida y
bebida.
Cada línea deberá mostrar una combinación diferente.
"""