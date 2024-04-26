# Librerias Estandar
from typing import List

from motor.dominio.entidades import Pasajero

# Librerías de Terceros
import pandas as pd


def dto_df_survivor__entidad_pasajero(df: pd.DataFrame) -> List[Pasajero]:
    return [
        Pasajero(
            id=row["PassengerId"],
            sobreviviente=row["Survived"],
            clase=row["Pclass"],
            nombre=row["Name"],
            sexo=row["Sex"],
            edad=row["Age"],
            parche=row["Parch"],
            ticket=row["Ticket"],
            tarifa=row["Fare"],
            cabina=row["Cabin"],
            embarque=row["Embarked"],
        )
        for _, row in df.iterrows()
    ]


def dto_entidad_pasajero__df_survivor(pasajeros: List[Pasajero]) -> pd.DataFrame:
    data = []
    for pasajero in pasajeros:
        data.append(
            {
                "PassengerId": pasajero.id,
                "Survived": pasajero.sobreviviente,
                "Pclass": pasajero.clase,
                "Name": pasajero.nombre,
                "Sex": pasajero.sexo,
                "Age": pasajero.edad,
                "SibSp": pasajero.parche,
                "Parch": pasajero.parche,
                "Ticket": pasajero.ticket,
                "Fare": pasajero.tarifa,
                "Cabin": pasajero.cabina,
                "Embarked": pasajero.embarque,
            }
        )

    df = pd.DataFrame(data)
    return df
