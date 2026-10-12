try:
  entrada = input("Introduce un número entero positivo: ")
  num = int(entrada)

  if num <= 0:
    raise ValueError("El número debe ser estrictamente positivo (> 0).")

  if num == 1:
    print("El número 1 no se considera primo ni compuesto.")
  else:
    divisibles = []
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        divisibles.append(i)
        break  # Con encontrar el primer divisor basta para saber que no es primo

    if not divisibles:
      print(f"¡El número {num} es primo!")
    else:
      print(
          f"No es primo porque es divisible por {divisibles[0]} (y"
          " posiblemente otros)."
      )

except ValueError as e:
  print(f"Error de validación: {e}")