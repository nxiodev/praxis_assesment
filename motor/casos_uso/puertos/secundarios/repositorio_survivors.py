# Librerias Estandar
from typing import List
from abc import abstractmethod, ABC

from ....dominio.entidades import entidades_survivors as e


class RepositorioSurvivors(ABC):

    @abstractmethod
    def get_df(self):
        """
        Funcion que obtiene el DataFrame
        :return: DataFrame
        """
        ...

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
    def get_gt(self, df, value: int | float | bool | str, column: str):
        """
        Funcion que obtiene mayor que de una columna y valor dado
        :param df: DataFrame a filtrar
        :param value: valor a comparar
        :param column: columna a comparar
        :return: el mismo DataFrame filtrado
        """
        ...

    @abstractmethod
    def get_lt(self, df, value: int | float | bool | str, column: str):
        """
        Funcion que obtiene menor que de una columna y valor dado
        :param df: DataFrame a filtrar
        :param value: valor a comparar
        :param column: columna a comparar
        :return: el mismo DataFrame filtrado
        """
        ...

    @abstractmethod
    def get_gte(self, df, value: int | float | bool | str, column: str):
        """
        Funcion que obtiene mayor o igual que de una columna y valor dado
        :param df: DataFrame a filtrar
        :param value: valor a comparar
        :param column: columna a comparar
        :return: el mismo DataFrame filtrado
        """
        ...

    @abstractmethod
    def get_lte(self, df, value: int | float | bool | str, column: str):
        """
        Funcion que obtiene menor o igual que de una columna y valor dado
        :param df: DataFrame a filtrar
        :param value: valor a comparar
        :param column: columna a comparar
        :return: el mismo DataFrame filtrado
        """
        ...
