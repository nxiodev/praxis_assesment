# Librerias Estandar
from dataclasses import dataclass


@dataclass
class Pasajero:
    id: int
    sobreviviente: int
    clase: int
    nombre: str
    sexo: str
    edad: float
    parche: int
    ticket: str
    tarifa: float
    cabina: str
    embarque: str
