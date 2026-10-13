try:
  edad = int(input("Introduce tu edad para verificar tus permisos: "))

  if edad < 0:
    print("Error: La edad no puede ser negativa.")
  elif edad >= 18:
    print("Puedes conducir: Moto de poca cilindrada, moto de gran cilindrada y coche.")
  elif edad >= 16:
    print("Puedes conducir: Moto de poca cilindrada y moto de gran cilindrada.")
  elif edad >= 14:
    print("Puedes conducir: Moto de poca cilindrada.")
  else:
    print("No puedes conducir ningún vehículo.")
except ValueError:
  print("Error: Debes introducir un número entero válido.")