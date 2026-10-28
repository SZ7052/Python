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
class Entradasuperior(Exception):
    pass
class NumeroNegativo(Exception):
    pass


entradas=25
opcion=0

while opcion!=3 and entradas > 0:
    try:
        opcion=int(input("ingrese una opcion: "))
        if opcion==3:
            print("Saliendo...")
            break
        if opcion==1:
            try:
                entradascompra=int(input("ingrese un numero de entradas: "))
                if entradas>25:
                    raise Entradasuperior("No hay tantas entradas")
                if entradas<=0:
                    raise NumeroNegativo("Numero negativo")
                entradas-=entradascompra
                print("Compra Exitosa!")
                if entradas == 0:
                    print("No hay más entradas disponibles.")
                    break

            except NumeroNegativo as e:
                print(f"Error:{e}")
            except Entradasuperior as e:
                print(f"Error: {e}")
            except ValueError:
                print("Valor invalido")
        elif opcion==2:
            print(f"{entradas} entradas disponibles")
        else:
            print("Opcion invalida")



    except ValueError:
        print("Valor invalido")