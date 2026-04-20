def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    # TODO: Crear diccionario y agregarlo a la agenda
    agenda.append({"nombre":nombre, "telefono":telefono, "email":email})

    pass

def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    # TODO: Ordenar por nombre e imprimir en formato tabular
    # Pista: sorted(agenda, key=lambda c: c["nombre"])
    sortagenda = sorted(agenda, key=lambda c: c["nombre"])
    for val in sortagenda:
        print("\n",val["nombre"], "\nTelefono: ",val["telefono"],"\nEmail: ",val["email"])

    pass

def buscar_contacto(agenda, termino):
    # TODO: Retornar lista de contactos cuyo nombre contenga 'termino'
    # Pista: usa 'termino.lower() in contacto["nombre"].lower()'
    found = []
    for contacto in agenda:
        if contacto["nombre"].find(termino.lower()) != -1:
            found.append(contacto)
            #print("\n",contacto["nombre"], "\n",contacto["telefono"],"\n",contacto["email"])
    return found
    pass

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)
    if not resultados:
        print("No se encontró el contacto.")
        return
    # TODO: Si hay múltiples resultados, mostrarlos y pedir selección
    # TODO: Pedir nuevo teléfono y/o email (enter para no cambiar)
    selectedCont = resultados[0]
    instr = ""
    if len(resultados)>1:
        index = 1
        print("Multiples opciones detectadas, seleccione la opcion deseada:")
        for contacto in resultados:
            print(index, ") ", contacto["nombre"])
            index += 1
        index = int(input("Opcion seleccionada: "))-1
        if index < 0 or index > len(resultados)-1:
            print("Opcion invalida, cancelando accion")
            return
        selectedCont = resultados[index]

    instr = input("Seleccione nuevo telefono (ENTER para no cambiar):")
    if (instr != ""):
        selectedCont["telefono"] = instr
    instr = input("Seleccione nuevo email (ENTER para no cambiar)")
    if (instr != ""):
        selectedCont["email"] = instr
    pass

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    # TODO: Buscar y eliminar
    resultados = buscar_contacto(agenda, nombre)
    if not resultados:
        print("No se encontro el contacto")
        return
    selContacto = resultados[0]
    if len(resultados)>1:
        index = 1
        print("Multiples opciones detectadas, seleccione la opcion deseada:")
        for contacto in resultados:
            print(index, ") ", contacto["nombre"])
            index += 1
        index = int(input("Opcion seleccionada: "))-1
        if index < 0 or index > len(resultados)-1:
            print("Opcion invalida, cancelando accion")
            return
        selContacto = resultados[index]

    agenda.remove(selContacto)
    pass

def exportar_csv(agenda):
    # TODO: Imprimir cada contacto como: nombre,telefono,email
    print("nombre,telefono,email")
    for contacto in agenda:
        print(contacto["nombre"], ", ", contacto["telefono"],", ",contacto["email"])
    pass

def estadisticas(agenda):
    # TODO: Total de contactos
    # TODO: Contar dominios de email (parte después del @)
    print("Total de contactos: ", len(agenda))
    dominioCount = {}
    for contacto in agenda:
        lugarArroba = contacto["email"].find("@")
        if lugarArroba != -1:
            if contacto["email"][lugarArroba:] in dominioCount.keys():
                dominioCount[contacto["email"][lugarArroba:]] += 1
            else:
                dominioCount[contacto["email"][lugarArroba:]] = 1

    print("Dominios de email guardados:")
    for dominio, num in dominioCount.items():
        print(dominio, ": ", num)
    pass

def menu():
    agenda = []
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Exportar CSV")
        print("7. Estadísticas")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            listar_contactos(agenda)
        elif opcion == "3":
            termino = input("Buscar: ")
            resultados = buscar_contacto(agenda, termino)
            if resultados:
                for c in resultados:
                    print(f"  {c['nombre']} - {c['telefono']} - {c['email']}")
            else:
                print("Sin resultados.")
        elif opcion == "4":
            editar_contacto(agenda)
        elif opcion == "5":
            eliminar_contacto(agenda)
        elif opcion == "6":
            exportar_csv(agenda)
        elif opcion == "7":
            estadisticas(agenda)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
