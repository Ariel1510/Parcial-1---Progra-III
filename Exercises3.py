#Un hotel de playa cuenta con un recepcionista que se encarga de
#presentar a los clientes las opciones de habitaciones disponibles junto
#con sus precios. Tras la elección de la habitación, el recepcionista
#solicita los datos personales del cliente y el número de noches que
#permanecerá en el hotel. Finalmente, entrega al cliente una factura
#detallada con el total de los gastos.
#Adicionalmente, los clientes pueden solicitar servicios extra,
#como el uso de la piscina o la cancha de golf, que tienen un costo
#adicional. Implementa esta funcionalidad en tu programa

class Hotel:

    def __init__(self, tipHab, precioHab, nombre, apellido, telefono, noches, extras):
        self._extras = 10.0
        self.tipoHab = tipHab
        self.precioHabitacion = precioHab
        self.nombreCliente = nombre
        self.ApeCliente = apellido
        self.telCliente = telefono
        self.numNoches = noches
        self.numExtras = extras
        self.precioExtras = extras * self._extras
        self.ventaFinal = (noches * precioHab) + self.precioExtras

    def mostrar_informacion(self):
        print(f"\n~~~~~~~~~~ INFORMACIÓN DE LA HABITACIÓN ~~~~~~~~~~")
        print(f"Nombre del cliente: {self.nombreCliente}")
        print(f"Apellido del cliente: {self.ApeCliente}")
        print(f"Teléfono del cliente: {self.telCliente}")
        print(f"Servicios extra pedidos: {self.numExtras}")
        print(f"Noches de su estancia: {self.numNoches}")
        print(f"El tamaño de la habitación es {self.tipoHab} con un costo de ${self.precioHabitacion}")
        print(f"Costo por servicio extra: ${self._extras}")
        print(f"Total a pagar: ${self.ventaFinal}")


def obtenerDatos():
    habitacio = []
    print("BIENVENIDO, seleccione el tipo de habitación que desea: ")
    print("Opción (1): Habitación pequeña con una cama y baño privado. PRECIO $30 la noche")
    print("Opción (2): Habitación mediana con dos camas y baño privado. PRECIO $45 la noche")
    print("Opción (3): Habitación grande con una cama matrimonial y una cama mediana, cocina privada y baño privado. PRECIO $60")
    
    tipoHabitacion = int(input("Escoja el tipo de habitación que desea usando (1), (2) o (3): "))
    if tipoHabitacion == 1:
        tipHab = "Pequeña"
        precioHab = 30
    elif tipoHabitacion == 2:
        tipHab = "Mediana"
        precioHab = 45
    elif tipoHabitacion == 3:
        tipHab = "Grande"
        precioHab = 60
    else:
        print("El valor ingresado es incorrecto")
        return []
    
    print("~~~~ REGISTRO DEL CLIENTE ~~~~")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    noches = int(input("Ingrese el número de noches que se quedará: "))
    extras = int(input("""Puede elegir servicios extra como: 
                    Bar a habitación, servicio a la habitación, uso de recreación del hotel (piscinas, cancha de golf, zonas extremas y arcade)
                    esto por un costo adicional de $10 por cada servicio.
                    ¿Desea adquirir servicios extra? coloque cuántos por ejemplo: 1, 2, etc: """))
    
    habitacion = Hotel(tipHab, precioHab, nombre, apellido, telefono, noches, extras)
    habitacio.append(habitacion)
    return habitacio


def devolverDatos(habitacio):
    for habitacion in habitacio:
        habitacion.mostrar_informacion()


cliente = obtenerDatos()
devolverDatos(cliente)



