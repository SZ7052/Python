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
Entradas = 25
Disponible = True


    while Disponible:
        print("1.Comprar entradas.")
        print("2.Mostrar entradas disponibles.")
        print("3.Salir.")
try:
numeromenu=int(input("Ingrese un numero de menu: "))

if numeromenu == 1:
    numeroentradas = int(input("Ingrese un numero de entradas: "))
    if Entradas <= 0:
        Disponible = False
        exception
    else:
        Entradas -= numeroentradas
elif numeromenu == 2:
    print(f"{Entradas} entradas disponibles.")
elif numeromenu == 3:
    print("Saliendo...")
else:
    print("Valor incorrecto")
except ValueError:
    print("Valor incorrecto")


# Definimos excepciones personalizadas para cumplir con el enunciado
class CantidadInvalidaError(Exception):
    pass


class DemasiadasEntradasError(Exception):
    pass


# Variables iniciales
entradas_disponibles = 25
activo = True

while activo:
    print("\n--- MENÚ TEATRO ---")
    print("1. Comprar entradas.")
    print("2. Mostrar entradas disponibles.")
    print("3. Salir.")

    try:
        # Controlamos que la opción del menú sea un número entero
        numeromenu = int(input("Ingrese un número de menú: "))

        if numeromenu == 1:
            try:
                # Solicitar número de entradas
                numeroentradas = int(input("Ingrese el número de entradas que desea comprar: "))

                # Validar cantidad <= 0
                if numeroentradas <= 0:
                    raise CantidadInvalidaError("La cantidad de entradas debe ser mayor que 0.")

                # Validar si se solicitan más entradas de las disponibles
                if numeroentradas > entradas_disponibles:
                    raise DemasiadasEntradasError(
                        f"No hay suficientes entradas. Quedan {entradas_disponibles} disponibles.")

                # Si todo es correcto, actualizamos las entradas
                entradas_disponibles -= numeroentradas
                print(f"¡Compra realizada con éxito! Entradas restantes: {entradas_disponibles}")

                # Opcional: Si se acaban las entradas, podemos finalizar
                if entradas_disponibles == 0:
                    print("¡Se han agotado todas las entradas!")
                    activo = False

            except ValueError:
                print("Error: Debe introducir un valor numérico válido para las entradas.")
            except CantidadInvalidaError as e:
                print(f"Error: {e}")
            except DemasiadasEntradasError as e:
                print(f"Error: {e}")

        elif numeromenu == 2:
            print(f"-> Actualmente hay {entradas_disponibles} entradas disponibles.")

        elif numeromenu == 3:
            print("Saliendo del programa. ¡Hasta pronto!")
            activo = False

        else:
            # Control de opción de menú no válida (sin usar excepciones, tal como pedía el enunciado)
            print("Error: Opción de menú no válida. Elija un número entre 1 y 3.")

    except ValueError:
        print("Error: Debe introducir un número entero válido para seleccionar la opción del menú.")