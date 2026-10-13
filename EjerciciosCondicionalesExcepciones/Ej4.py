try:
  clave = input("Introduce tu clave: ")
  if clave == "python123":
    print("Acceso concedido.")
  else:
    print("Acceso denegado.")
except Exception as e:
  print(f"Ha ocurrido un error: {e}")