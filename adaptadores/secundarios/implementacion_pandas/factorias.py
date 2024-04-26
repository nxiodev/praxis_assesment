from motor.casos_uso.puertos.secundarios import repositorio_survivors as ps

# Proyecto
from .repositorios_impl import RepositorioSurvivorsImpl


def construir_repo_survivors(data_path) -> ps.RepositorioSurvivors:
    return RepositorioSurvivorsImpl(data_path)
