"""Una biblioteca ofrece préstamos de libros a través de una tarjeta
impresa que contiene los datos de la persona que realiza el préstamo. El
sistema de préstamos registra la fecha en que se retira el libro y la fecha
límite para su devolución. Realiza un programa que solvente esto de
una manera más eficaz.
 Implementar la sección de devolución la cual si la fecha excede la
que devolución se dará una sanción"""

"""La forma en la que realice este ejercicio la pense en base a que se facilitaran o simplificaran un poco los procesos
esto tambien tomando en cuenta de que los multiples def que hemos usado, cada uno tiene un trabajo en especifico y que nos ayuda a 
hacer de forma mas ordenada cada accion"""
prestamosActivos = []

class Prestamo:
    def __init__(self, usuario, entidad, identificador, titulo, fechaInicio, duracion):
        self.usuario = usuario
        self.entidad = entidad
        self.identificador = identificador
        self.titulo = titulo
        self.fechaInicio = fechaInicio
        self.duracion = int(duracion)
#Funcion que nos permite mostrar la informacion adquirida
    def mostrarInformacion(self):
        print("Usuario: ", self.usuario)
        print("Entidad: ", self.entidad)
        print("Identificador: ", self.identificador)
        print("Título del Libro: ", self.titulo)
        print("Fecha de Inicio: ", self.fechaInicio)
        print("Duración (días): ", self.duracion)
#Funcion que nos permite evaluar el estado del prestamos segun los dias que han pasado y comparando la duracion del prestamo que escogimos
    def evaluarDevolucion(self):
        diasPasados = int(input("Ingrese el número de días transcurridos desde el inicio del préstamo: "))
        if diasPasados > self.duracion:
            print("Se ha excedido el límite de préstamo, se aplicará una sanción.")
        else:
            print("El préstamo está dentro del período permitido para la devolución.")
#Con esta funcion hacemos la creacion del prestamo, obteniendo todos los datos que se necesitan recopilar a la hora de realizar un prestamo
def crearPrestamo():
    usuario = input("Ingrese su nombre completo: ")
    entidad = input("Ingrese su entidad: ")
    identificador = input("Ingrese su identificador: ")
    deseo = input("¿Desea realizar un préstamo? (S/N): ").upper()
    if deseo == "S":
        titulo = input("Ingrese el título del libro: ")
        fechaInicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        duracion = input("Ingrese la duración del préstamo en días: ")
    else:
        titulo = "Ninguno"
        fechaInicio = "Ninguno"
        duracion = "0"

    nuevoPrestamo = Prestamo(usuario, entidad, identificador, titulo, fechaInicio, duracion)
    nuevoPrestamo.mostrarInformacion()
    prestamosActivos.append(nuevoPrestamo)
    return nuevoPrestamo

# Crear un nuevo préstamo
prestamo1 = crearPrestamo()

# Evaluar la devolución del libro
prestamo1.evaluarDevolucion()