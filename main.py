def ingresarRepartidores():
    cantidad = int(input("Cantidad de repartidores a ingresar: "))
    repartidores = {}
    i = 1
    while i <= cantidad:
        print(f"\nIngreso del repartidor #{i}")
        nombre = input("Nombre: ")
        if nombre in repartidores:
            print("Ya existe ese repartidor.")
            continue
        zona = input("Zona: ")
        paquetes = int(input("Cantidad de paquetes entregados: "))
        repartidores[nombre] = {
            "zona": zona,
            "paquetes": paquetes
        }
        i += 1
    return repartidores


def mostrarOriginal(repartidores):
    print("\n=== REGISTRO ORIGINAL ===")
    for nombre in repartidores:
        print(f"Nombre: {nombre}")
        print(f"  Zona: {repartidores[nombre]['zona']}")
        print(f"  Paquetes entregados: {repartidores[nombre]['paquetes']}")


def quickSort(nombres, repartidores):
    if len(nombres) <= 1:
        return nombres
    else:
        pivote = repartidores[nombres[0]]['paquetes']
        menores = [x for x in nombres[1:] if repartidores[x]['paquetes'] > pivote]
        iguales = [x for x in nombres if repartidores[x]['paquetes'] == pivote]
        mayores = [x for x in nombres[1:] if repartidores[x]['paquetes'] < pivote]
        return quickSort(menores, repartidores) + iguales + quickSort(mayores, repartidores)


def mostrarRanking(repartidores):
    ordenados = quickSort(list(repartidores.keys()), repartidores)
    print("\n=== RANKING DE REPARTIDORES ===")
    for i in range(len(ordenados)):
        nombre = ordenados[i]
        print(f"{i+1}. {nombre} - Paquetes: {repartidores[nombre]['paquetes']}")


def buscarRepartidor(repartidores):
    nombre = input("Nombre a buscar: ")
    if nombre in repartidores:
        print(f"Zona: {repartidores[nombre]['zona']}")
        print(f"Paquetes: {repartidores[nombre]['paquetes']}")
    else:
        print("Repartidor no encontrado.")


def estadisticasExtras(repartidores):
    if not repartidores:
        print("No hay datos.")
        return
    total = sum([repartidores[n]["paquetes"] for n in repartidores])
    promedio = total / len(repartidores)
    print(f"Total de paquetes entregados: {total}")
    print(f"Promedio de paquetes por repartidor: {promedio:.2f}")



repartidores = {}

while True:
    print("\n--- MENÚ ---")
    print("1. Ingresar repartidores")
    print("2. Mostrar registro original")
    print("3. Ordenar y mostrar ranking")
    print("4. Buscar repartidor")
    print("5. Estadísticas extras")
    print("6. Salir")
    opcion = input("Opción: ")

    match opcion:
        case "1":
            repartidores = ingresarRepartidores()
        case "2":
            mostrarOriginal(repartidores)
        case "3":
            mostrarRanking(repartidores)
        case "4":
            buscarRepartidor(repartidores)
        case "5":
            estadisticasExtras(repartidores)
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida.")
