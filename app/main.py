import time
import zoneinfo
from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from db import create_all_tables
from .routers import resultados

app = FastAPI(lifespan=create_all_tables)

# Incluir el router de resultados electorales
app.include_router(resultados.router)

@app.middleware("http")
async def log_request_headers(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in: {process_time} seconds")
    return response

# Ejemplo de autenticación básica
security = HTTPBasic()

@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == "eduardo" and credentials.password == "123456":
        return {"message": "Hello, Eduardo!"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")