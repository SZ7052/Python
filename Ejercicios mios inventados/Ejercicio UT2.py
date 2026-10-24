"""
Ejercicio: Gestión de compra en un supermercado
Crea un programa en Python que simule el proceso de cobro en la caja de un supermercado.
El programa debe pedir al usuario el precio unitario de un producto y la cantidad comprada,
acumulando el total de la compra hasta que el usuario decida finalizar.
El programa debe:
Manejar errores de entrada con try-except:
    Capturar si el usuario introduce un valor no numérico (por ejemplo, texto o letras).
Validar los datos ingresados:
    Comprobar que tanto el precio como la cantidad sean números estrictamente positivos (> 0).
Si se introduce un valor menor o igual a cero, se debe mostrar un mensaje de error y pedir el dato de nuevo.
Bucle interactivo:
    Repetir el proceso de solicitar precio y cantidad para múltiples productos hasta que el usuario introduzca un precio igual a 0 para finalizar la compra.
Descuento por volumen (condicionales):
    Al finalizar la compra, si el importe total acumulado supera los $50€, se aplicará un $10% de descuento sobre el total.
Resultado final:
    Mostrar por pantalla el total sin descuento, el importe del descuento aplicado (si procede) y el total final a pagar.
"""



total_compra = 0.0

print("--- CAJA DE SUPERMERCADO ---")
print("Introduce un precio de 0 para finalizar la compra.\n")

while True:
    try:
        precio = float(input("Introduce el precio unitario del producto (0 para salir): "))

        if precio == 0:
            print("Finalizando la compra...")
            break
        elif precio < 0:
            print("Error: El precio no puede ser negativo. Inténtalo de nuevo.\n")
            continue

        cantidad = int(input("Introduce la cantidad comprada: "))

        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor que cero.\n")
            continue

        subtotal = precio * cantidad
        total_compra += subtotal
        print(f"-> Añadido con éxito. Subtotal parcial: {subtotal:.2f} EUR\n")

    except ValueError:
        print("Error: Entrada no válida. Debes introducir un número.\n")

print("\n" + "=" * 30)
print("TICKET DE COMPRA FINAL")
print("=" * 30)
print(f"Total acumulado: {total_compra:.2f} EUR")

descuento = 0.0

if total_compra > 50:
    descuento = total_compra * 0.10
    print(f"¡Descuento aplicado (10%): -{descuento:.2f} EUR!")
else:
    print("No se alcanza el mínimo de 50 EUR para aplicar descuento.")

total_final = total_compra - descuento
print(f"TOTAL A PAGAR: {total_final:.2f} EUR")
print("=" * 30)
