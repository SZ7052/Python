print("--- MENÚ DE OPCIONES ---")
print("1. Ver perfil")
print("2. Editar perfil")
print("3. Salir")

try:
  opcion = int(input("Introduce el número de la opción (1-3): "))

  if opcion == 1:
    print("Has seleccionado: Ver perfil.")
  elif opcion == 2:
    print("Has seleccionado: Editar perfil.")
  elif opcion == 3:
    print("Saliendo del programa...")
  else:
    print("Error: Opción no válida. Debe ser un número entre 1 y 3.")
except ValueError:
  print("Error: Debes introducir un número entero válido.")