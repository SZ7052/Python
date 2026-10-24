#Calcular el precio final de un producto con descuento

#Crear un programa que pida el precio de un producto y el porcentaje de descuento,
# y que calcule y muestre el precio final.

precio = float(input("Introduce el precio del producto: "))
descuento = float(input("Introduce el porcentaje de descuento: "))

precio_final = precio - (precio * descuento / 100)

print("El precio final es:", precio_final, "euros")