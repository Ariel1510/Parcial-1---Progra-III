"""
Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.
"""

"""
Se abordó esta solución debido a que como se necesita tanto guardar datos de autos nuevos por parte de la administracion
y tambien por parte de los clientes se necesita registrar las rentas que estos mismos quieran, con los datos del auto
rentado y los datos personales del cliente
"""
class Renta:
    def __init__(self, marcaAuto, modeloAuto, anioAuto, colorAuto, tipoMotorAuto, 
                 transmisionAuto, PrecioCompra, kilometrajeAuto, placaAuto, renta):
        self.marca = marcaAuto
        self.modelo = modeloAuto
        self.anio = anioAuto
        self.color = colorAuto
        self.tipoMotor = tipoMotorAuto
        self.transmision = transmisionAuto
        self.precioCompra = float(PrecioCompra)
        self.kilometraje = kilometrajeAuto
        self.placa = placaAuto.upper()
        self.renta = float(renta)

    def salidaAutosNuevos(self):
        print(f"---------------------------------------------\n"+
              "Datos del auto: \n"+
              "..............................................\n"+
              f"Marca: {self.marca}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Color: {self.color}\n"+
              f"Tipo de motor: {self.tipoMotor}\n"+
              f"Kilometraje: {self.kilometraje} KM\n"+
              f"Placa: {self.placa}\n"+
              f"Año: {self.anio}\n"+
              f"Transmisión: {self.transmision}\n"+
              f"Precio de Compra: {self.precioCompra}\n"+
              f"Precio de Renta: {self.renta}\n"+
              "..............................................\n")


def registrarAuto():
    A_marca = input("Ingrese la marca del auto: ")
    A_modelo = input("Ingrese el modelo del auto: ")
    A_anio = input("Ingrese el año del auto: ")
    A_color = input("Ingrese el color del auto: ")
    A_motor = input("Ingrese el tipo de motor del auto: ")
    A_transmision = input("Ingrese el tipo de transmisión del auto: ")
    A_kilometraje = input("Ingrese el kilometraje del auto: ")
    A_placa = input("Ingrese el número de placa del auto: ")
    A_precio = input("Ingrese el precio de compra del auto: ")
    A_renta = input("Ingrese el precio de renta: ")
    return Renta(A_marca, A_modelo, A_anio, A_color, A_motor,
                 A_transmision, A_precio, A_kilometraje, A_placa, A_renta)


def registrarCliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dui = input("Ingrese su DUI: ")
    return nombre, apellido, edad, dui

#Esa funcion es la encargada de hacer la ejecución de los prints y los input llamandoloes, esto se hace acá
#debido a la pregunta inicial si es de parte de la administracion o de parte del cliente

def inicial():
    registrados = []
    while True: #el while nos permite ingresar datos indefinidos

        tipo_usuario = input("¿Es usted un cliente (Ingrese C) o administrador (Ingrese A)? ").upper()
        if tipo_usuario == "A": #por lo mismo antes mencionado se hace evaluación mediante if 
            auto = registrarAuto()
            registrados.append(auto)
            auto.salidaAutosNuevos()
        elif tipo_usuario == "C":
            if not registrados:
                print("No hay autos disponibles para alquilar.")
            else:
                nombre, apellido, edad, dui = registrarCliente()
                print("Autos disponibles:")
                 #mediante el for y con un index accedemos dentro de los datos de los autos registrados por la administración y gracias a eso el cliente
                #puede tener una lista ennumerada de datos de autos para escoger a la hora de rentar 
                for index, auto in enumerate(registrados):
                    print(f"{index + 1}. {auto.marca} {auto.modelo} ({auto.anio}) - {auto.color}")
                seleccionAuto = int(input("Ingrese el número del auto que desea alquilar: ")) - 1
                if 0 <= seleccionAuto < len(registrados):
                    autoSeleccionado = registrados[seleccionAuto]
                    print("------------------------------------------"+
                          "\nHas seleccionado el siguiente auto:")
                    autoSeleccionado.salidaAutosNuevos()
                    print(f"Datos del cliente:\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDUI: {dui}\n"+
                          "------------------------------------------")
                    break
                else:
                    print("Selección no válida.")
        else:
            print("Opción no válida. Intente nuevamente.")
inicial()
