# Ejercicios de Programación en Python:
# Condicionales-Excepciones
# Nota:
# Todos los ejercicios deben tener control de excepciones capturando los errores si el usuario
# introduce un valor de tipo no válido.


# Ejercicio 1: Verificación de edad
# Pide al usuario que introduzca su edad. Valida que sea un número entero positivo. Si la edad
# es mayor o igual a 18, muestra un mensaje indicando que es mayor de edad. Si no, indica que
# es menor de edad.
# class Numeropositvo(Exception):
#     pass
#
# try:
#     edad = int(input("Ingrese edad: "))
#     if edad < 0:
#         raise Numeropositvo("El numero tiene que ser positivo")
#     if edad >= 18:
#         print("es mayor de edad")
#     else:
#         print("es menor de edad")
# except Numeropositvo as e:
#     print(f"Error:{e}")
# except ValueError:
#     print ("Error, please enter numeric input")



# Ejercicio 2: Comparación de dos números
# Solicita al usuario dos números enteros. Muestra cuál es mayor, cuál es menor o si son
# iguales.


# try:
#     n1 = int(input("Introduce un numero: "))
#     n2 = int(input("Introduce otro numero: "))
#     if n1 > n2:
#         print(f"El {n1} es mayor que el {n2}")
#     elif n1 < n2:
#         print(f"El {n1} es menor que el {n2}")
#     else:
#         print("Los numeros son igual")
# except ValueError:
#     print("Error, please enter numeric input")

# Ejercicio 3: Validación de nota
# Pide al usuario una nota numérica entre 0 y 10. Valida que sea un número decimal dentro
# del rango. Clasifica la nota como:
# Suspenso (0-4.9)
# Aprobado(5-6.9)
# Notable (7-8.9)
# Sobresaliente (9-10)

# class Entreunoydies(Exception):
#     pass
#
# try:
#     nota=float(input("Ingrese nota: "))
#     if 0>nota>10:
#         raise Entreunoydies("Nota Invalida")
#     if 9<=nota<=10:
#         print("Sobresaliente")
#     elif 7<=nota<=8.9:
#         print("Notable")
#     elif 5<=nota<=6.9:
#         print("Notable")
#     else:
#         print("Suspenso")
# except Entreunoydies as e:
#     print(f"Error: {e}")
# except ValueError:
#     print("Valor invalido")
# Ejercicio 4: Acceso con clave
# Pide al usuario que introduzca una clave. Si la clave coincide con "python123", muestra un
# mensaje de acceso concedido. Si no, muestra acceso denegado.


# try:
#     clave=str(input("Introduce la clave: "))
#     if clave=="python123":
#         print("acceso concedido")
#     else :
#         print("acceso denegado")
#
# except ValueError :
#     print("Error : Valor incorrecto")

# Ejercicio 5: Menú de selección
# Muestra un menú con tres opciones:
# 1. Ver perfil
# 2. Editar perfil
# 3. Salir
# Pide al usuario que introduzca el número de la opción. Muestra un mensaje según la opción
# elegida. Si introduce un valor no válido, muestra un mensaje de error.

opciones=0

while opciones!=3:
    try:
        print("1.Ver perfil")
        print("2.Editar perfil")
        print("3.Salir")
        opciones=int(input("Introduce un numero: "))
        if opciones==3:
            print("Saliendo..")
            break
        match opciones:
            case 1:
                print("tu perfil")
            case 2:
                print("editando...")
    except ValueError:
        print("Valor invalido")


# Ejercicio 6: Validación de número par o impar
# Solicita al usuario un número entero. Valida que sea correcto. Muestra si el número es par o
# impar.

# try:
#     n1=int(input("Introduce un numero: "))
#     if n1%2==0:
#         print("par")
#     else:
#         print("impar")
# except ValueError:
#     print("Error : Valor incorrecto")

# Ejercicio 7: Verificación de permisos para conducir según edad
# Solicita al usuario su edad. Según la edad, muestra qué tipo de
# vehículo puede conducir:
# - Menor de 14: no puede conducir
# - 14 o más: moto de poca cilindrada
# - 16 o más: moto de gran cilindrada
# - 18 o más: coche

try:
    numero = int(input("Ingrese su edad: "))
    if numero>= 18:
        print("coche")
    elif 18>numero>=16:
        print("moto de gran")
    elif 16>numero>=14:
        print("moto de poca")
    else:
        print("no puede conducir")

except ValueError:
    print("Valor invalido")
