#
# Ejercicio 1: Verificación de número primo con control
# de errores
# Escribe un programa que solicite al usuario un número entero positivo y determine si es
# primo. El programa debe:
# - Validar que el número sea entero y positivo.
# - Lanzar una excepción si el valor no cumple con estas condiciones.
# - Mostrar si el número es primo o no, explicando por qué (por ejemplo, “No es primo
# porque es divisible por 3”).
class NumeroPositivo(Exception):
    pass


try:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        raise NumeroPositivo("Numero negativo")
    if numero % 1==0 and numero % numero ==0:
        print("Es un numero primo")
    else :
        print("No es un numero primo")
except NumeroPositivo as e:
    print(f"Error:{e}")
except ValueError:
    print("numero invalido")

# Ejercicio 2: Conversor de divisas con control de errores
# Crea un programa que convierta una cantidad en euros a otra divisa
# (USD, GBP o JPY).
# El usuario debe introducir:
# - La cantidad en euros.
# - La divisa destino.
# El programa debe:
# - Validar que la cantidad sea un número positivo.
# - Validar que la divisa esté entre las permitidas.
# - Manejar excepciones si el usuario introduce datos incorrectos.
class OpcionNoValido(Exception):
    pass
class NumeroNegativo(Exception):
    pass
opcion=0

while opcion != 4:
    print("1.Cambio a USD")
    print("2.Cambio a GBP")
    print("3.Cambio a JPY")
    print("4.Salir")
    try:
        opcion = int(input("Ingrese un numero: "))
        if opcion < 0:
            raise NumeroNegativo("Numero negativo")
        if opcion<1 or opcion>4:
            raise OpcionNoValido("Opcion fuera de rango")
        if opcion==4:
            print("Saliendo...")
            break
        match opcion:
            case 1:
                numero = float(input("Ingrese un numero: "))
                conversion=numero*1.115
                print(round(conversion,2))
            case 2:
                numero = float(input("Ingrese un numero: "))
                conversion=numero*0.837
                print(round(conversion,2))
            case 3:
                numero = float(input("Ingrese un numero: "))
                conversion=numero*162.50
                print(round(conversion,2))



    except NumeroNegativo as e:
        print(f"Error:{e}")
    except OpcionNoValido as e:
        print(f"Error:{e}")
    except ValueError:
        print("numero invalido")
# Ejercicio 3: Cálculo de raíces reales de una ecuación
# cuadrática
# Solicita al usuario los coeficientes a, b y c de una ecuación cuadrática de la forma: ax² + bx +
# c = 0
# El programa debe:
# - Validar que a no sea cero (ya que no sería una ecuación cuadrática).
# - Calcular el discriminante D = b² - 4ac.
# - Lanzar una excepción si no hay raíces reales (es decir, si el discriminante es negativo).
# - Mostrar las raíces reales si existen.



# Ejercicio 4: Simulador de cajero automático
# Simula un cajero automático que permite retirar dinero de una cuenta.
# El usuario debe introducir:
# - Saldo inicial.
# - Cantidad a retirar.
# El programa debe:
# - Validar que el saldo y la cantidad sean números positivos.
# - Comprobar si hay suficiente saldo.
# - Lanzar una excepción si se intenta retirar más de lo disponible.
# - Mostrar el saldo restante.



# Ejercicio 5: Calculadora de operaciones con manejo
# múltiple de excepciones
# Crea una calculadora que permita al usuario introducir dos números
# y una operación (+, -, *,/). El programa debe:
# - Validar que los números sean válidos.
# - Manejar la división por cero.
# - Manejar operaciones no reconocidas.
# - Usar try-except con múltiples bloques para capturar distintos errores.

