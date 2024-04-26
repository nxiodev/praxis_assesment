import os
from adaptadores.secundarios.implementacion_pandas.factorias import construir_repo_survivors
from motor.casos_uso.factoria import constructor_manager_survivors

from adaptadores.secundarios.implementacion_pandas import mapper

survivors_data_path = os.environ.get("SURVIVORS_DATA_PATH", "")
repositorio_survivors = construir_repo_survivors(survivors_data_path)
motor = constructor_manager_survivors(repositorio_survivors)

pasajeros_df = motor.get_df()

# Quitar Miss Mr y Master
patron = r'(?:Mr|Mrs|Miss|Master|Dr)\.\s'
pasajeros_df["Name"] = pasajeros_df["Name"].str.replace(patron, "", regex=True)

# Obtener los pasajeros que sobrevivieron (1)
survivors = motor.filter_df_value_col(pasajeros_df, "Survived", 1)
survivors = mapper.dto_entidad_pasajero__df_survivor(survivors)

# Obtener los pasajeros que no sobrevivieron (2)
not_survivors = motor.filter_df_value_col(pasajeros_df, "Survived", 0)
not_survivors = mapper.dto_entidad_pasajero__df_survivor(not_survivors)

# Obtener los pasajeros que son mujeres
pasajeros_mujeres = motor.filter_df_value_col(pasajeros_df, "Sex", "female")
# Se convierte de nuevo a df
pasajeros_mujeres = mapper.dto_entidad_pasajero__df_survivor(pasajeros_mujeres)
# total de Sex(female) (3)
total_pasajeros_mujeres = pasajeros_mujeres["Sex"].count()

# Obtener los pasajeros que son hombres
pasajeros_hombres = motor.filter_df_value_col(pasajeros_df, "Sex", "male")
# Se convierte de nuevo a df
pasajeros_hombres = mapper.dto_entidad_pasajero__df_survivor(pasajeros_hombres)
# total de Sex(male) (3)
total_pasajeros_hombres = pasajeros_hombres["Sex"].count()

# Obtener los pasajeros que son mujeres mayores de 65 años
age_filter_config = {"gt": 65}

female_65_survivors = motor.filter_df_value_col(pasajeros_mujeres, "Age", age_filter_config.get("gt"),
                                                **age_filter_config)
female_65_survivors = mapper.dto_entidad_pasajero__df_survivor(female_65_survivors)

try:
    female_65_survivors = motor.filter_df_value_col(female_65_survivors, "Survived", 1)
    female_65_survivors = mapper.dto_entidad_pasajero__df_survivor(female_65_survivors)
    # total de mujeres mayores a 65 años y sobrevivientes (4)
    total_female_65_surviors = female_65_survivors["Sex"].count()
except Exception as e:
    print(f"Error: {e}")
    total_female_65_surviors = 0

male_65_survivors = motor.filter_df_value_col(pasajeros_hombres, "Age", age_filter_config.get("gt"),
                                              **age_filter_config)
male_65_survivors = mapper.dto_entidad_pasajero__df_survivor(male_65_survivors)
try:
    male_65_survivors = motor.filter_df_value_col(male_65_survivors, "Survived", 1)
    male_65_survivors = mapper.dto_entidad_pasajero__df_survivor(male_65_survivors)
    # total de hombres mayores a 65 años y sobrevivientes (4)
    total_male_65_surviors = male_65_survivors["Sex"].count()
except Exception as e:
    print(f"Error: {e}")
    total_male_65_surviors = 0

# total de pasajeros que son mujeres y hombres mayores de 65 años y de primera clase (5)
try:
    female_65_survivors_1_class = motor.filter_df_value_col(female_65_survivors, "Pclass", 1)
    female_65_survivors_1_class = mapper.dto_entidad_pasajero__df_survivor(female_65_survivors_1_class)
    total_female_65_survivors_1_class = female_65_survivors_1_class["Pclass"].count()
except Exception as e:
    print(f"Error: {e}")
    total_female_65_survivors_1_class = 0

# total de pasajeros que son mujeres y hombres mayores de 65 años y de primera clase (5)
try:
    male_65_survivors_1_class = motor.filter_df_value_col(male_65_survivors, "Pclass", 1)
    male_65_survivors_1_class = mapper.dto_entidad_pasajero__df_survivor(male_65_survivors_1_class)
    total_male_65_survivors_1_class = male_65_survivors_1_class["Pclass"].count()
except Exception as e:
    print(f"Error: {e}")
    total_male_65_survivors_1_class = 0

# total de pasajeros mujeres que son mayores a 18 no sobrevivientes y de primera clase (6)
age_filter_config = {"gt": 18}

pasjeros_mujeres_not_survivors = motor.filter_df_value_col(not_survivors, "Sex", "female")
pasjeros_mujeres_not_survivors = mapper.dto_entidad_pasajero__df_survivor(pasjeros_mujeres_not_survivors)

try:
    pasajeros_mujers_not_survivors_1_class = motor.filter_df_value_col(pasjeros_mujeres_not_survivors, "Pclass", 1)
    pasajeros_mujers_not_survivors_1_class = mapper.dto_entidad_pasajero__df_survivor(
        pasajeros_mujers_not_survivors_1_class)
    total_mujeres_18_not_survivors_1_class = pasajeros_mujers_not_survivors_1_class["Pclass"].count()
except Exception as e:
    print(f"Error: {e}")
    total_mujeres_18_not_survivors_1_class = 0

# total de pasajeros hombres que son mayores a 18 no sobrevivientes y de primera clase (6)
pasjeros_hombres_not_survivors = motor.filter_df_value_col(not_survivors, "Sex", "male")
pasjeros_hombres_not_survivors = mapper.dto_entidad_pasajero__df_survivor(pasjeros_hombres_not_survivors)

try:
    pasajeros_hombres_not_survivors_1_class = motor.filter_df_value_col(pasjeros_hombres_not_survivors, "Pclass", 1)
    pasajeros_hombres_not_survivors_1_class = mapper.dto_entidad_pasajero__df_survivor(
        pasajeros_hombres_not_survivors_1_class)
    total_hombres_18_not_survivors_1_class = pasajeros_hombres_not_survivors_1_class["Pclass"].count()
except Exception as e:
    print(f"Error: {e}")
    total_hombres_18_not_survivors_1_class = 0

print(
    f"1. Sobrevivientes \n {survivors} \n "
    f"2. No sobrevivientes \n {not_survivors} \n "
    f"3. Total de mujeres: {total_pasajeros_mujeres} \n "
    f"3. Total de hombres: {total_pasajeros_hombres} \n "
    f"4. Total de mujeres mayores a 65 años y sobrevivientes: {total_female_65_surviors} \n"
    f"4. Total de hombres mayores a 65 años y sobrevivientes: {total_male_65_surviors} \n"
    f"5. Total de mujeres mayores a 65 años y de primera clase: {total_female_65_survivors_1_class} \n"
    f"5. Total de hombres mayores a 65 años y de primera clase: {total_male_65_survivors_1_class} \n"
    f"6. Total de mujeres mayores a 18 años no sobrevivientes y de primera clase: {total_mujeres_18_not_survivors_1_class} \n"
    f"6. Total de hombres mayores a 18 años no sobrevivientes y de primera clase: {total_hombres_18_not_survivors_1_class} \n"
    f"El punto 7 se hizo desde el principio, remplazar los valores en los nombres Mr Miss Master \n {pasajeros_df['Name']}"

)
