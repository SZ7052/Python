try:
  numero = int(input("Introduce un número entero: "))

  if numero % 2 == 0:
    print(f"El número {numero} es par.")
  else:
    print(f"El número {numero} es impar.")
except ValueError:
  print("Error: Debes introducir un número entero válido.")