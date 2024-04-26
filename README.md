# PRAXIS GLOBE ASSESSMENT

El ejercicio propuesto es el siguiente:

https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv

Header PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked 

Para esos datos, generar las siguientes “salidas”.

- ##### Obtener los sobrevivientes 1
- ##### Obtener los nos sobrevivientes 0
- ##### Obtener el total de Sex (male,female)
- ##### Obtener el total de Sex (male,female) mayores a 65 años y Sobrevivientes
- ##### Obtener el total de Sex (male,female) mayores a 65 años y Sobrevivientes, además que sean de primera clase Pclass
- ##### Obtener el total de Sex (male,female) mayores a 18 años y No Sobrevivientes, además que sean de primera clase Pclass
- ##### Limpiar el campo Name  quitar (Mr,Mrs,.,etc)

***
# Proyecto

En este proyecto intenté poner en práctica los conocimientos que he adquirido en mi carrera profesional para resolver el ejercicio propuesto, utilizando clean code y buenas prácticas de programación, cumpliendo los estándares de calidad pep8.

## Estrucutra del proyecto

El proyecto está estructurado de la siguiente manera:

En los adaptadores se encuentran las implementaciones de librerías de terceros
en los adaptadores secundarios, así como el uso de las mismas en los primarios
```
├── adaptadores/ 
│   ├── primarios/
│   ├── secundarios/
```
En el motor se realiza una interfaz la cual permite aislar la lógica de negocio de la implementación de la misma, 
permitiendo que se pueda cambiar la implementación sin afectar la lógica de negocio
Esto permite cambiar de proveedor en este caso la librería pandas por otra usando la misma interfaz

El diseño de la arquitectura usa diferentes capas y patrones de diseño que van desde factorias, constructores, repositorios y managers
y se basa en el principio de responsabilidad única, abierto/cerrado, inversión de dependencias, segregación de interfaces y el principio de sustitución de Liskov

Se presenta la estructura del motor:

```
├── motor/
│   ├── casos_de_uso/
│   │  ├── puertos/
│   │   │   ├── primarios/managers*
│   │   │   ├── secundarios/repositorios*
│   │  ├── servicios/interfaz*
│   │  ├── factoria*

│   ├── dominio/
│   │   ├── entidades/data_structures*
│   │   ├── excepciones/
│   ├── compartidos/
```

Para más información del patrón de diseño de puertos y adaptadores se puede consultar el siguiente enlace:

```
https://apiumhub.com/es/tech-blog-barcelona/arquitectura-hexagonal/
```

también pueden consultar un repositorio personal en el cual aplico ese patrón para una api rest
```
https://github.com/nxiodev/django_arq_hex_example
```
***
## Instalación y uso

Para instalar el proyecto se debe clonar el repositorio y crear un entorno virtual con python

```sh
git clone
```

```sh
python -m venv venv
```
Se activa el ambiente:
```sh
source venv/bin/activate
```
Se instalan dependencias
```sh
pip install -r requirements.txt
```

Para ejectuar los resultados del ejercicio se debe ejecutar el siguiente comando:

```sh
python main.py
```
***
# Resultados

Los resultados se muestran en consola, se obtiene la información solicitada en el ejercicio

### Resumen

Se obtiene la información solicitada en el ejercicio
- **Bonus:**
  - Se generó un código con diseño de alta calidad
- **Mejoras:**
  - Se puede implementar test de comportamiento dentro del motor para verificar la lógica de negocio

