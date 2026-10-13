try:
  edad = int(input("Introduce tu edad: "))
  if edad < 0:
    print("Error: La edad no puede ser un número negativo.")
  elif edad >= 18:
    print("Eres mayor de edad.")
  else:
    print("Eres menor de edad.")
except ValueError:
  print("Error: Debes introducir un número entero válido.")