def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    # TODO: Crear el diccionario del producto y agregarlo a la lista
    producto={"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Se ha agregado el producto al inventario")
    pass

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    # TODO: Recorrer el inventario e imprimir cada producto
    for producto in inventario:
        print(f"{producto["nombre"]:<20}, {producto["precio"]:>10}, {producto["cantidad"]:>10}")
    pass

def buscar_producto(inventario, nombre):
    # TODO: Buscar y retornar el producto cuyo nombre coincida
    # Retornar None si no se encuentra
    for producto in inventario:
        if producto["nombre"]==nombre:
            return producto
    else:
        return None
    pass

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        # TODO: Actualizar la cantidad del producto
        producto["cantidad"]=nueva_cantidad
        print("Se ha actualizado la cantidad del producto:", producto["nombre"])
        pass

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    # TODO: Buscar el producto y eliminarlo de la lista
    # Pista: usa inventario.remove(producto)
    producto=buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"Se ha eliminado el producto {producto["nombre"]} del inventario ")
    else:
        print(f"No se econtró el proucto {nombre}")
        return None
    pass

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    # TODO: Calcular e imprimir:
    # - Total de productos distintos
    # - Valor total (sum de precio * cantidad)
    # - Producto más caro y más barato
    print("Total de productos distintos: ", len(inventario))
    print("Valor total: ", sum(producto["precio"]*producto["cantidad"] for producto in inventario))
    producto_caro= max(inventario, key=lambda x: x["precio"])
    producto_barato=min(inventario, key=lambda x: x["precio"])
    print("Producto más caro: ", producto_caro["nombre"])
    print("Poducto más barato: ", producto_barato["nombre"])
    pass

def menu():
    inventario = []
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Resumen")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("No encontrado.")
        elif opcion == "4":
            actualizar_cantidad(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            resumen(inventario)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
