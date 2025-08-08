class Repartidor:
    def __init__(self, nombre,paquetes,zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona
    def __str__(self):
        return self.nombre + " " + self.paquetes + " " + self.zona

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = {}

    def ingresar(self):
        print("=== Ingreso de Repartidor ===")
        nombreAux = input("Ingrese el nombre del repartidor: ")
        if not nombreAux.lower() not in self.repartidores:
            print("Ese repartidor ya existe.")
            return

        try:
            paquetesAux = int(input("Ingrese la cantidad de paquetes entregados: "))
            if paquetesAux < 0:
                print("La cantidad no puede ser negativa.")
                return
            nuevo = Repartidor(nombreAux, paquetesAux)
            self.repartidores[nombreAux.lower()] = nuevo
            print("Repartidor agregado correctamente.")
        except ValueError:
            print("Cantidad invalida. Debe ser un numero entero.")

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            mayores = [x for x in lista[1:] if x.paquetes > pivote.paquetes]
            iguales = [x for x in lista if x.paquetes == pivote.paquetes]
            menores = [x for x in lista[1:] if x.paquetes < pivote.paquetes]
            return self.quick_sort(mayores) + iguales + self.quick_sort(menores)

    def mostrar_ranking(self):
        print("=== Ranking de Repartidores ===")
        ordenados = self.ordenar_por_paquetes()
        i = 1
        for r in ordenados:
            print(f"{i}. {r}")
            i += 1