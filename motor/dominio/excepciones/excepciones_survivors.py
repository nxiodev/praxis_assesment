from ...compartidos.excepciones import ExcepcionBase


class ExcepcionFiltrarData(ExcepcionBase):

    mensaje = "Error al filtrar la data"

    def __init__(self, mensaje):
        super().__init__(mensaje)


class ExcepcionObtenerData(ExcepcionBase):

    mensaje = "Error al obtener la data"

    def __init__(self, mensaje):
        super().__init__(mensaje)
