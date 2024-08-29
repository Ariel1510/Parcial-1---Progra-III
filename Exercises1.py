"""
Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.
En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código.
"""

class Consultorio:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.edad = 0
        self.peso = 0.0
        self.frecuencia_cardiaca = 0
        self.presion_arterial = ""
        self.motivo_consulta = ""
        self.estado = "Registrado"
        self.fecha_consulta = ""

    def actualizar(self):
        self.estado = "Sala de Espera"
        return self.estado

def mostrar_info(paciente):
    print("Nombre: ", paciente.nombre)
    print("Edad: ", paciente.edad)
    print("Peso: ", paciente.peso)
    print("Frecuencia Cardíaca: ", paciente.frecuencia_cardiaca)
    print("Presión Arterial: ", paciente.presion_arterial)
    print("Motivo de Consulta: ", paciente.motivo_consulta)
    print("Fecha de consulta: ", paciente.fecha_consulta)
    print("Estado: ", paciente.estado) 

def registrar(paciente):
    print("Registro de Paciente en el consultorio")
    paciente.edad = int(input("Ingrese la edad del paciente: "))
    paciente.peso = float(input("Peso del paciente (kg): "))
    paciente.frecuencia_cardiaca = int(input("Frecuencia cardiaca del paciente (bpm): "))
    paciente.presion_arterial = input("Presión Arterial: ")
    paciente.motivo_consulta = input("Motivo de consulta: ")
    paciente.fecha_consulta = input("Fecha de Consulta: ")
    print("Registro completado")

def main():
    registrados = []

    while True:
        print("Sistema de Gestión del Consultorio")
        nombreP = input("Ingrese el nombre del paciente: ")

        paciente_encontrado = None
        for paciente in registrados:
            if paciente.nombre == nombreP:
                paciente_encontrado = paciente
                break
        
        if paciente_encontrado:
            print("---------------------------------------------\n"+
                  "Paciente encontrado en la base")
            mostrar_info(paciente_encontrado)
        else:
            print("---------------------------------------------\n"+
                  "Paciente no encontrado, haciendo el registro")
            nuevo_paciente = Consultorio(nombre=nombreP)
            registrar(nuevo_paciente)
            registrados.append(nuevo_paciente)
            print(f"Paciente {nuevo_paciente.nombre} registrado exitosamente.")

if __name__ == "__main__":
    main()
