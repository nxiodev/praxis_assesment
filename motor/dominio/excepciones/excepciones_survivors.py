# Proyecto
from ...compartidos.excepciones import ExcepcionBase


class ExcepcionFiltrarData(ExcepcionBase):
    mensaje = "Error al filtrar la data"


class ExcepcionObtenerData(ExcepcionBase):
    mensaje = "Error al obtener la data"
