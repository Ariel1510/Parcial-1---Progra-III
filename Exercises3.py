#Un hotel de playa cuenta con un recepcionista que se encarga de
#presentar a los clientes las opciones de habitaciones disponibles junto
#con sus precios. Tras la elección de la habitación, el recepcionista
#solicita los datos personales del cliente y el número de noches que
#permanecerá en el hotel. Finalmente, entrega al cliente una factura
#detallada con el total de los gastos.
#Adicionalmente, los clientes pueden solicitar servicios extra,
#como el uso de la piscina o la cancha de golf, que tienen un costo
#adicional. Implementa esta funcionalidad en tu programa

class Hotel():

    def __init__(self, tipHab,precioHab, nombre, apellido, telefono, noches, extras):
            self._extras = 10.0
            self.tipoHab = tipHab
            self.precioHabitacion = precioHab
            self.nombreCliente = nombre
            self.ApeCliente = apellido
            self.telCliente = telefono
            self.numNoches = noches
            self.numExtras = extras
            self.precioExtras = extras * Hotel.extra()
            self.ventaFinal = (noches*precioHab)+Hotel.precioExtras

    def mostrar_información(self):
        print(f"\n~~~~~~~~~~ INFORMACIÓN DE LA HABITACION ~~~~~~~~~~")
        print(f"Nombre del cliente: {self.nombreCliente}")
        print(f"Apellido del cliente: {self.ApeCliente}")
        print(f"Telefono del cliente: {self.telCliente}")
        print(f"Servicios extra pedidos: {self.numExtras}")
        print(f"Noches de su estancia: {self.numNoches}")
        print(f"El tamaño de la habitacion es {self.tipoHab} con un costo de ${self.precioHabitacion}")
        print(f"Costo por servicio extra: {self._extras}")
        print(f"Total a pagar: {self.ventaFinal}")
        
    

    def obtenerDatos():
        habitacio = []
        print("BIENVENIDO, seleccione el tipo de habitación que desea: ") 
        print("Opcion (1): Habitacion pequeña con una cama y baño privado. PRECIO $30 la noche")
        print("Opcion (2): Habitación mediana con dos camas y baño privado. PRECIO $45 la noche")
        print("Opcion (3): Habitación grande con una cama matrimonial y una cama mediana, cocina privada y baño privado. Precio $60")
        tipoHabitacion = int(input("Escoja el tipo de habitación que desea usando (1), (2) o (3): "))
        if tipoHabitacion == 1:
            print("~~~~ REGISTRO DEL CLIENTE ~~~~")
            tipHab = "Pequeña"
            precioHab = 30
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            noches = int(input("Ingrese el numero de noches que se quedara: "))
            extras = int(input("""Puede elegir servicios extra como: 
                            Bar a habitacion, servicio a la habitacion, uso de recreacion del hotel(piscinas, cancha de golf, zonas extremas y arcade)
                            esto por un costo adicional de $10 por cada servicio
                                ¿Desea adquirir servicios extra? coloque cuanto por ejemplo: 1, 2, etc: """))
        elif tipoHabitacion == 2:
            print("~~~~ REGISTRO DEL CLIENTE ~~~~")
            tipHab = "Mediana"
            precioHab = 45
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            noches = int(input("Ingrese el numero de noches que se quedara: "))
            extras = int(input("""Puede elegir servicios extra como: 
                            Bar a habitacion, servicio a la habitacion, uso de recreacion del hotel(piscinas, cancha de golf, zonas extremas y arcade)
                            esto por un costo adicional de $10 por cada servicio
                                ¿Desea adquirir servicios extra? coloque cuanto por ejemplo: 1, 2, etc: """)) 
        elif tipoHabitacion == 3:
            print("~~~~ REGISTRO DEL CLIENTE ~~~~")
            tipHab = "Grande"
            precioHab = 55
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            noches = int(input("Ingrese el numero de noches que se quedara: "))
            extras = int(input("""Puede elegir servicios extra como: 
                            Bar a habitacion, servicio a la habitacion, uso de recreacion del hotel(piscinas, cancha de golf, zonas extremas y arcade)
                            esto por un costo adicional de $10 por cada servicio
                                ¿Desea adquirir servicios extra? coloque cuanto por ejemplo: 1, 2, etc: """))
        else:
            print("El valor ingresado es incorrecto")
        habitacion = Hotel(tipHab, precioHab, nombre, apellido, telefono, noches, extras)
        habitacio.append(habitacion)
        return habitacio
    
    def devolverDatos(habitacio):
        for habitacion in habitacio:
            habitacion.mostrar_informacion()

    cliente = obtenerDatos()
    mostrar_información(cliente)


