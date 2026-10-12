try:
  saldo_inicial = float(input("Introduce el saldo inicial de la cuenta (€): "))
  if saldo_inicial < 0:
    raise ValueError("El saldo inicial no puede ser un valor negativo.")

  retiro = float(input("Introduce la cantidad que deseas retirar (€): "))
  if retiro < 0:
    raise ValueError("La cantidad a retirar no puede ser un valor negativo.")

  if retiro > saldo_inicial:
    raise ValueError(
        "Fondos insuficientes: La cantidad a retirar supera el saldo disponible"
        f" ({saldo_inicial} €)."
    )

  saldo_restante = saldo_inicial - retiro
  print(f"Retiro realizado con éxito. Saldo restante: {saldo_restante:.2f} €")

except ValueError as e:
  print(f"Error en la operación del cajero: {e}")