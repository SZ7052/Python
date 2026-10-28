listaNombres = ["Natalia", "Estela", "Natalia", "Infanta"]

listaNombres2 = ["Elena", "Natalia" , "Tania", "Juana"]

listaNombresCompuestos = []

for nombre in listaNombres:
    for nombre2 in listaNombres2:
        print(nombre, nombre2)
        if nombre != nombre2:
            try:
                if (nombre + " " + nombre2) == "Infanta Elena":
                    raise ValueError
            except ValueError as e:
                print("IES en Galapagar con estudios de formación profesional.")

            listaNombresCompuestos.append(nombre + " " + nombre2)

print("Ha generado ", len(listaNombresCompuestos), " opciones válidas.")