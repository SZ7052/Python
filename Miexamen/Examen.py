class HorasNoValidas(Exception):
    pass
class Nohayvehiculos(Exception):
    pass




numero_plazas_libres=10
tarifa_por_hora=2.5
estancia_parking_max=24
Coste=0

opcion=0
registrar=True

while opcion!=4:
    print("1.Registrar entrada de vehiculo")
    print("2.Registrar salida de vehiculo")
    print("3.Mostrar estado del parking")
    print("4.Finalizar programa")

    try:
        opcion=int(input("Dime Opcion: "))
        if opcion==1:
            while registrar:
                if numero_plazas_libres>0:
                    try:
                        n_horas=int(input("Ingrese el numero de horas: "))
                        if n_horas>estancia_parking_max:
                                raise HorasNoValidas("N de horas de estancia no permitido")

                        else:
                            Coste=tarifa_por_hora*n_horas
                            print(f"{Coste}€")
                            numero_plazas_libres-=1
                            registrar=False
                    except HorasNoValidas as e:
                        print(f"Error: {e}")

                    except ValueError:
                        print("Debe introducir un valor numerico")
                else:
                    print("No hay plazas disponibles")


        elif opcion==2:
            if numero_plazas_libres<10:
                numero_plazas_libres+=1
                print("Se ha registrado un vehiculo")

            if numero_plazas_libres==10:
                raise Nohayvehiculos("No hay vehiculos en el parking y volver al menu principal")

        elif opcion==3:
                plazas_ocupadas= 10 - numero_plazas_libres
                print(f"Plazas libres:{numero_plazas_libres}")
                print(f"Plazas ocupadas:{plazas_ocupadas}")
                Porcentaje = (10 - numero_plazas_libres) * 10
                print(f"Porcentaje: {Porcentaje}%")
        elif opcion==4:
            break
        else:
            print("Opcion invalida")

    except Nohayvehiculos as e:
        print(f"Errore: {e}")
        continue
    except ValueError:
        print("Debe introducir un valor numerico")