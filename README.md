# Base de Datos Relacional de Personas Electas en México (2018-2023)

Este proyecto implementa una base de datos relacional para almacenar y gestionar información sobre las personas electas en México entre 2018 y 2023. La base de datos está diseñada para facilitar la consulta y análisis de los resultados electorales utilizando Python 3.9.21 y FastAPI [standard].

## Estructura del Proyecto

```
/
├── db.py                          # Configuración y conexión a la base de datos
├── import_data.py                 # Script para importar los datos en la base de datos
├── models.py                       # Definición de los modelos ORM con SQLAlchemy
├── resultados_electorales.sqlite3  # Archivo de la base de datos SQLite3
├── app/                            # Aplicación FastAPI
│   ├── __init__.py                 # Inicialización del módulo
│   ├── main.py                     # Punto de entrada de la API
│   ├── routers/                    # Rutas de la API
│   │   ├── __init__.py              # Inicialización del módulo de rutas
│   │   ├── resultados.py            # Endpoints relacionados con los resultados electorales
```

## Requisitos

- Python 3.9.21
- FastAPI [standard]
- SQLAlchemy
- SQLite3
- Uvicorn

### Instalación de dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```sh
pip install fastapi[standard] sqlalchemy sqlite3 uvicorn
```

## Uso

### Ejecutar la API
Para iniciar la API con Uvicorn, ejecuta:

```sh
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

### Importar Datos a la Base de Datos

Antes de ejecutar la API, asegúrate de importar los datos con el siguiente comando:

```sh
python import_data.py
```

## Descripción de la Base de Datos

La base de datos `resultados_electorales.sqlite3` contiene información estructurada sobre las personas electas en México entre 2018 y 2023. Se modela mediante SQLAlchemy y se organiza para consultas eficientes mediante FastAPI.

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si deseas colaborar, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.

## Contacto

Para cualquier consulta o colaboración, puedes contactar al autor en: **eduardobareapoot@outlook.com**.