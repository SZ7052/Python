try:
  nota = float(
      input("Introduce una nota numérica entre 0 y 10 (puedes usar decimales): ")
  )

  if 0 <= nota <= 10:
    if nota < 5:
      print("Suspenso")
    elif nota < 7:
      print("Aprobado")
    elif nota < 9:
      print("Notable")
    else:
      print("Sobresaliente")
  else:
    print("Error: La nota debe estar comprendida entre 0 y 10.")
except ValueError:
  print("Error: Debes introducir un valor numérico válido.")