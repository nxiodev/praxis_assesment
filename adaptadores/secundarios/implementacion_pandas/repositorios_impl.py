# Librerias Estandar
from dataclasses import dataclass
from typing import List


from motor.dominio.entidades import Pasajero, entidades_survivors as e
from motor.casos_uso.puertos.secundarios import repositorio_survivors as ps
from motor.dominio.excepciones import excepciones_survivors as ex

import pandas as pd

from . import mapper as mp


@dataclass
class RepositorioSurvivorsImpl(ps.RepositorioSurvivors):

    def __init__(self, data_path: str):
        self._df = pd.read_csv(data_path)

    def get_df(self):
        return self._df

    def get_gt(self, df, value: int | float | bool | str, column: str):
        return df[df[column] > value]

    def get_lt(self, df, value: int | float | bool | str, column: str):
        return df[df[column] < value]

    def get_gte(self, df, value: int | float | bool | str, column: str):
        return df[df[column] >= value]

    def get_lte(self, df, value: int | float | bool | str, column: str):
        return df[df[column] <= value]

    def filter_df_value_col(self, df, column: str, value: str | int | float | bool, **kwargs) -> List[e.Pasajero]:
        """
        Funcion que filtra un DataFrame por una columna y un valor, ademas permite agregar argumentos adicionales para operaciones de comparacion
        :param df: DataFrame a filtrar
        :param column: columna por la que se filtrara el DataFrame
        :param value: valor por el que se filtrara la columna
        :param kwargs: argumentos adicionales para operaciones de comparacion gt, lt, gte, lte
        :return: lista de pasajeros que cumplen con la condicion
        """
        if "gt" in kwargs:
            data_frame = self.get_gt(df, value, column)
        elif "lt" in kwargs:
            data_frame = self.get_lt(df, value, column)
        elif "gte" in kwargs:
            data_frame = self.get_gte(df, value, column)
        elif "lte" in kwargs:
            data_frame = self.get_lte(df, value, column)
        else:
            data_frame = df[df[column] == value]
        return mp.dto_df_survivor__entidad_pasajero(data_frame)
