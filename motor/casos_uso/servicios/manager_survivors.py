# Librerias Estandar
from dataclasses import dataclass
from typing import List

# Proyecto
from ..puertos.secundarios.repositorio_survivors import RepositorioSurvivors
from ...dominio.entidades.entidades_survivors import Pasajero
from ..puertos.primarios.manager_survivors import ManagerSurvivors
from ...dominio.excepciones import excepciones_survivors as ex


@dataclass
class ManagerSurvivorsImpl(ManagerSurvivors):
    def __init__(self, repositorio_survivors: RepositorioSurvivors):
        self._repo_survivors = repositorio_survivors

    def filter_df_value_col(self, df, column: str, value: str | int | float | bool, **kwargs) -> List[Pasajero]:
        try:
            return self._repo_survivors.filter_df_value_col(df=df, column=column, value=value, **kwargs)
        except ex.ExcepcionFiltrarData as e:
            raise ex.ExcepcionFiltrarData from e

    def get_df(self):
        try:
            return self._repo_survivors.get_df()
        except ex.ExcepcionObtenerData as e:
            raise ex.ExcepcionObtenerData from e
