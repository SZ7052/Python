"""
Ejercicio 1: Venta de entradas de teatro
Un teatro dispone inicialmente de 25 entradas disponibles. Desarrolla un programa en Python
que permita comprar entradas mediante un menú con las siguientes opciones:
1. Comprar entradas.
2. Mostrar entradas disponibles.
3. Salir.
Debes tener en cuenta que:
● Al seleccionar la opción Comprar entradas, el programa solicitará el número de
entradas que desea comprar el cliente.
● Si la venta es correcta, se actualizará el número de entradas disponibles.
● El programa deberá repetirse hasta que el usuario seleccione la opción Salir.
● Tanto si el usuario introduce un valor no numérico, como si solicita una cantidad de
entradas menor o igual que cero o si solicita más entradas de las que quedan
disponibles, se debe controlar usando excepciones específicas.
● Además, el programa deberá controlar opciones de menú no válidas. (no es necesario
utilizar excepciones)
"""


class CantidadInvalidaError(Exception):
    pass


class DemasiadasEntradasError(Exception):
    pass


entradas = 25
disponible = True

while disponible and entradas > 0:
    print("\n1. Comprar entradas.")
    print("2. Mostrar entradas disponibles.")
    print("3. Salir.")

    try:
        numeromenu = int(input("Ingrese un numero de menu: "))

        if numeromenu == 1:
            try:
                numeroentradas = int(input("Ingrese un número de entradas a comprar: "))

                if numeroentradas <= 0:
                    raise CantidadInvalidaError("El número de entradas tiene que ser positivo.")

                if numeroentradas > entradas:
                    raise DemasiadasEntradasError("No hay suficientes entradas disponibles.")

                entradas -= numeroentradas
                print("¡Compra exitosa!")

                if entradas == 0:
                    print("No hay más entradas disponibles.")
                    disponible = False

            except ValueError:
                print("Error: Debe introducir un valor numérico válido para las entradas.")
            except CantidadInvalidaError as e:
                print(f"Error: {e}")
            except DemasiadasEntradasError as e:
                print(f"Error: {e}")

        elif numeromenu == 2:
            print(f"{entradas} entradas disponibles.")

        elif numeromenu == 3:
            print("Saliendo...")
            disponible = False

        else:
            print("Valor incorrecto, tiene que ser entre 1, 2 y 3.")

    except ValueError:
        print("Error: Debe introducir un número entero válido para el menú.")