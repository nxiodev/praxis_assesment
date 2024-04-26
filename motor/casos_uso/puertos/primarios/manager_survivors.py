# Librerias Estandar
from typing import List
from abc import abstractmethod, ABC

from ....dominio.entidades import entidades_survivors as e


class ManagerSurvivors(ABC):
    @abstractmethod
    def filter_df_value_col(self, df, column: str, value: str | int | float | bool, **kwargs) -> List[e.Pasajero]:
        """
        Funcion que filtra un DataFrame por una columna y un valor, ademas permite agregar argumentos adicionales para operaciones de comparacion
        :param df: DataFrame a filtrar
        :param column: columna por la que se filtrara el DataFrame
        :param value: valor por el que se filtrara la columna
        :param kwargs: argumentos adicionales para operaciones de comparacion gt, lt, gte, lte
        :return: lista de pasajeros que cumplen con la condicion
        """
        ...

    @abstractmethod
    def get_df(self):
        """
        Funcion que obtiene el DataFrame
        :return: DataFrame
        """
        ...
