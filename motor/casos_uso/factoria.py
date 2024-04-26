# Proyecto
from .puertos.secundarios import repositorio_survivors as repositorio
from .puertos.primarios import manager_survivors as manager
from .servicios import manager_survivors as servicio


def constructor_manager_survivors(repositorio_survivors: repositorio.RepositorioSurvivors) -> manager.ManagerSurvivors:
    return servicio.ManagerSurvivorsImpl(repositorio_survivors=repositorio_survivors)
