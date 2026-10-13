try:
  num1 = int(input("Introduce el primer número entero: "))
  num2 = int(input("Introduce el segundo número entero: "))

  if num1 > num2:
    print(f"El número mayor es {num1} y el menor es {num2}.")
  elif num2 > num1:
    print(f"El número mayor es {num2} y el menor es {num1}.")
  else:
    print("Ambos números son iguales.")
except ValueError:
  print("Error: Debes introducir números enteros válidos.")