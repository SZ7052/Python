preciosProductos = []
precio = 0
precioMedio = 0
condicionCumplida = 0
precioMayor = 0

try:
    while precio != 9999.99:
        precio = float(input("Ingresa un precio: "))
        if precio >= 0 and precio != 9999.99:
            preciosProductos.append(precio)

    for precio in preciosProductos:
        if precio >= 10: #Las condiciones tienen que cumplir todas la primera.
            print(precio)
            condicionCumplida += 1
            precioMedio += precio
            if precioMayor < precio:
                precioMayor = precio

    print("Productos que cumplen la condición: ", condicionCumplida)

    try:
        precioMedio /= condicionCumplida
        print("Precio medio: ", precioMedio)
    except ZeroDivisionError as e:
        print("Error: ", e)

    print("Precio mayor: ", precioMayor)

except ValueError as e:
    print("Error: ", e)