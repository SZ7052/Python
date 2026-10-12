import math

try:
  a = float(input("Introduce el coeficiente a: "))
  if a == 0:
    raise ValueError(
        "El coeficiente 'a' no puede ser cero (no sería una ecuación"
        " cuadrática)."
    )

  b = float(input("Introduce el coeficiente b: "))
  c = float(input("Introduce el coeficiente c: "))

  # Cálculo del discriminante D = b^2 - 4ac
  discriminante = (b**2) - (4 * a * c)

  if discriminante < 0:
    raise ValueError(
        f"No hay raíces reales porque el discriminante es negativo"
        f" ({discriminante})."
    )

  # Cálculo de las raíces
  x1 = (-b + math.sqrt(discriminante)) / (2 * a)
  x2 = (-b - math.sqrt(discriminante)) / (2 * a)

  if discriminante == 0:
    print(f"Existe una única raíz real: x = {x1}")
  else:
    print(f"Existen dos raíces reales: x1 = {x1} y x2 = {x2}")

except ValueError as e:
  print(f"Error: {e}")