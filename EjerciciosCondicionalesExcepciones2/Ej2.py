# Tasas de cambio de referencia
tasas_cambio = {"USD": 1.08, "GBP": 0.85, "JPY": 165.50}

try:
  euros = float(input("Introduce la cantidad en euros: "))
  if euros < 0:
    raise ValueError("La cantidad en euros no puede ser un número negativo.")

  divisa_destino = input(
      "Introduce la divisa destino (USD, GBP, JPY): "
  ).upper()
  if divisa_destino not in tasas_cambio:
    raise KeyError(
        f"La divisa '{divisa_destino}' no está permitida. Opciones válidas: USD,"
        " GBP, JPY."
    )

  resultado = euros * tasas_cambio[divisa_destino]
  print(f"{euros:.2f} EUR equivalen a {resultado:.2f} {divisa_destino}.")

except ValueError as ve:
  print(f"Error en el valor introducido: {ve}")
except KeyError as ke:
  print(f"Error en la divisa: {ke}")