"""
Ejercicio 5: Calcular descuento
Crea una función llamada `calcular_descuento` que reciba:
- precio_original (float)
- descuento (float), como argumento por palabra clave, con valor por defecto 10
La función debe devolver el precio final tras aplicar el descuento.
"""

def calcular_descuento(precio_original, descuento=10):
    desc=descuento/100

    return precio_original * (1-desc)

print(calcular_descuento(100,10))