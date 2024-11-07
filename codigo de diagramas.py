from datetime import date
from typing import List

class Consulta:
    def _init_(self, en_linea_o_cita: str, fecha_solicitud: date, cadena_sintomas: str, estado_solicitud: str):
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud
        self.doctor = None  # Relación con Doctor (uno a muchos)
        self.paciente = None  # Relación con Paciente (uno a muchos)


class Paciente:
    def _init_(self, id: str, nombre: str, edad: int, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.consultas: List[Consulta] = []  # Relación con Consulta (uno a muchos)
        
    def crear_perfil_de_paciente(self):
        pass
    
    def editar_perfil_de_paciente(self):