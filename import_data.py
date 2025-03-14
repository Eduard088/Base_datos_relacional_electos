# import_data.py

import pandas as pd
from sqlmodel import Session
from models import ResultadoElectoral, SexoEnum, CoalicionEnum
from db import engine

def import_resultados(csv_file: str):
    # Leer el CSV (asegúrate de que las columnas coincidan con las siguientes)
    df = pd.read_csv(csv_file)
    
    with Session(engine) as session:
        for index, row in df.iterrows():
            año = int(row['Año'])
            nombre_estado = row['Nombre_estado']
            cargo = row['Cargo']
            partido = row['Partido']
            nombre_candidato = row['Nombre_candidato']
            sexo_valor = str(row['Sexo']).strip()
            # Convertir a enum (asumiendo que en el CSV vienen "Hombre" o "Mujer")
            if sexo_valor.lower() == "hombre":
                sexo_enum = SexoEnum.HOMBRE
            else:
                sexo_enum = SexoEnum.MUJER

            coalicion_valor = str(row['Coalición']).strip()
            if coalicion_valor.lower() in ['sí', 'si']:
                coalicion_enum = CoalicionEnum.SI
            else:
                coalicion_enum = CoalicionEnum.NO

            formula = row['Formula']
            
            resultado = ResultadoElectoral(
                año=año,
                nombre_estado=nombre_estado,
                cargo=cargo,
                partido=partido,
                nombre_candidato=nombre_candidato,
                sexo=sexo_enum,
                coalicion=coalicion_enum,
                formula=formula
            )
            session.add(resultado)
        session.commit()
    print("Datos importados exitosamente.")

if __name__ == "__main__":
    csv_file = "/home/barea/limpieza/electos/{{cookiecutter.project_slug}}/data/final/datos_electorales_2015_2023_1.csv"
    import_resultados(csv_file)