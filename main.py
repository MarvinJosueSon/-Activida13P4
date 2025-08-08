class Repartidor:
    def __init__(self, nombre,paquetes,zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona
    def __str__(self):
        return self.nombre + " " + self.paquetes + " " + self.zona

