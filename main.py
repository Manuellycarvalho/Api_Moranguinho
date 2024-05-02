from fastapi import FastAPI, HTTPException, Depends, status , Response
from pydantic import BaseModel
from typing import Optional, List
from create_db import engine, Base, get_db
from sqlalchemy.orm import Session
from core.configs import settings
from api.v1.api import api_router
from . import crud, models, schemas

from models.moranguinho_models import Moranguinho


from models import moranguinho_models
from repositories import MoranguinhoRepository
from schemas import MoranguinhoSchema,MoranguinhoResponse,MoranguinhoRequest

app= FastAPI(title="API de moranguinho com Xampp")
app.include_router(api_router,prefix=settings.API_V1_STR)
models.moranguinho_models.Base.metadata.create_all(bind=engine)


@app.post("/api/moranguinhos", response_model=MoranguinhoResponse, status_code=status.HTTP_201_CREATED)
def create(request: MoranguinhoRequest, db: Session = Depends(get_db)):
    moranguinho = MoranguinhoRepository.save(db, Moranguinho(**request.dict()))
    return MoranguinhoResponse.from_orm(moranguinho)


@app.get("/api/moranguinhos", response_model=list[MoranguinhoResponse])
def find_all(db: Session = Depends(get_db)):
    moranguinhos = MoranguinhoRepository.find_all(db)
    return [MoranguinhoResponse.from_orm(moranguinho) for moranguinho in moranguinhos]

@app.get("/api/moranguinhos/{id}", response_model=MoranguinhoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    moranguinho = MoranguinhoRepository.find_by_id(db, id)
    if not moranguinho:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Moranguinho não encontrado"
        )
    return MoranguinhoResponse.from_orm(moranguinho)

@app.delete("/api/moranguinhos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not MoranguinhoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Moranguinho não encontrado"
        )
    MoranguinhoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/moranguinhos/{id}", response_model=MoranguinhoResponse)
def update(id: int, request: MoranguinhoRequest, db: Session = Depends(get_db)):
    if not MoranguinhoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Moranguinho não encontrado"
        )
    moranguinho = MoranguinhoRepository.save(db, Moranguinho(id=id, **request.dict()))
    return MoranguinhoResponse.from_orm(moranguinho)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level="info", reload=True)