from fastapi import APIRouter, HTTPException, status, Query
from sqlmodel import select
from db import SessionDep
from models import ResultadoElectoral, ResultadoElectoralCreate, ResultadoElectoralUpdate

router = APIRouter()

@router.post("/resultados", response_model=ResultadoElectoral, status_code=status.HTTP_201_CREATED, tags=["resultados"])
async def create_resultado(resultado_data: ResultadoElectoralCreate, session: SessionDep):
    resultado = ResultadoElectoral(**resultado_data.dict())
    session.add(resultado)
    session.commit()
    session.refresh(resultado)
    return resultado

@router.get("/resultados/{resultado_id}", response_model=ResultadoElectoral, tags=["resultados"])
async def read_resultado(resultado_id: int, session: SessionDep):
    resultado = session.get(ResultadoElectoral, resultado_id)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultado electoral no encontrado")
    return resultado

@router.patch("/resultados/{resultado_id}", response_model=ResultadoElectoral, tags=["resultados"])
async def update_resultado(resultado_id: int, resultado_data: ResultadoElectoralUpdate, session: SessionDep):
    resultado = session.get(ResultadoElectoral, resultado_id)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultado electoral no encontrado")
    for key, value in resultado_data.dict(exclude_unset=True).items():
        setattr(resultado, key, value)
    session.add(resultado)
    session.commit()
    session.refresh(resultado)
    return resultado

@router.delete("/resultados/{resultado_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["resultados"])
async def delete_resultado(resultado_id: int, session: SessionDep):
    resultado = session.get(ResultadoElectoral, resultado_id)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resultado electoral no encontrado")
    session.delete(resultado)
    session.commit()
    return {"detail": "Resultado electoral eliminado"}

@router.get("/resultados", response_model=list[ResultadoElectoral], tags=["resultados"])
async def list_resultados(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Cantidad de registros a mostrar")
):
    resultados = session.exec(select(ResultadoElectoral).offset(skip).limit(limit)).all()
    return resultados
