from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum

# Enum para el campo Sexo
class SexoEnum(str, Enum):
    HOMBRE = "Hombre"
    MUJER = "Mujer"

# Enum para el campo Coalición
class CoalicionEnum(str, Enum):
    SI = "Sí"
    NO = "No"

# Modelo principal: ResultadoElectoral
class ResultadoElectoral(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    año: int
    nombre_estado: str
    cargo: str
    partido: str
    nombre_candidato: str
    sexo: SexoEnum
    coalicion: CoalicionEnum
    formula: str

# Modelo para la creación (input)
class ResultadoElectoralCreate(SQLModel):
    año: int
    nombre_estado: str
    cargo: str
    partido: str
    nombre_candidato: str
    sexo: SexoEnum
    coalicion: CoalicionEnum
    formula: str

# Modelo para la actualización (input parcial)
class ResultadoElectoralUpdate(SQLModel):
    año: Optional[int] = None
    nombre_estado: Optional[str] = None
    cargo: Optional[str] = None
    partido: Optional[str] = None
    nombre_candidato: Optional[str] = None
    sexo: Optional[SexoEnum] = None
    coalicion: Optional[CoalicionEnum] = None
    formula: Optional[str] = None
