try:
  num1 = float(input("Introduce el primer número: "))
  num2 = float(input("Introduce el segundo número: "))
  operacion = input(
      "Introduce la operación a realizar (+, -, *, /): "
  ).strip()

  if operacion == "+":
    resultado = num1 + num2
  elif operacion == "-":
    resultado = num1 - num2
  elif operacion == "*":
    resultado = num1 * num2
  elif operacion == "/":
    if num2 == 0:
      raise ZeroDivisionError("No está permitido dividir entre cero.")
    resultado = num1 / num2
  else:
    raise ValueError(f"La operación '{operacion}' no está reconocida.")

  print(f"El resultado de la operación es: {resultado}")

except ValueError as ve:
  print(f"Error de valor o de operación: {ve}")
except ZeroDivisionError as zde:
  print(f"Error matemático: {zde}")
except Exception as e:
  print(f"Ha ocurrido un error inesperado: {e}")