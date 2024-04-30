from typing import List 
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import Session
from sqlalchemy.future import select


from models.moranguinho_models import MoranguinhoModel
from schemas.moranguinho_schema import MoranguinhoSchema
from core.deps import get_session
from main import get_db

from create_db import SessionLocal, engine

router = APIRouter()



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MoranguinhoSchema) 
async def post_moranguinho(moranguinho: MoranguinhoSchema, db: Session = Depends(get_db)):
    nova_moranguinho = MoranguinhoModel(nome=moranguinho.nome, residencia=moranguinho.residencia,genero=moranguinho.genero,ocupacao=moranguinho.ocupacao,aparencia=moranguinho.aparencia,personalidade=moranguinho.personalidade,animais_de_estimacao=moranguinho.animais_de_estimacao)
    db.add(nova_moranguinho)
    await db.commit()
    
    return db.query()

@router.get("/", response_model=List[MoranguinhoSchema])
async def get_moranguinho(db: Session = Depends(get_db)):
    async with db as session:
        query = select(MoranguinhoModel)
        result = await session.execute(query)
        moranguinho: List[MoranguinhoModel] = result.scalars().all()
        
        return db.query(moranguinho).all()
    

@router.get("/{moranguinho_id}", response_model=MoranguinhoSchema, status_code=status.HTTP_200_OK)
async def get_moranguinho(moranguinho_id: int, db: Session= Depends(get_db)):
    async with db as session:
        query = select(MoranguinhoModel).filter(MoranguinhoModel.id==moranguinho_id)
        result = await session.execute(query)
        moranguinho = result.scalar_one_or_none()
        
        if moranguinho:
            return moranguinho
        else:
            raise HTTPException(detail="moranguinho Não Encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
        
        
@router.put("/{moranguinho_id}", response_model=MoranguinhoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_carro(moranguinho_id: int, moranguinho: MoranguinhoSchema, db: Session = Depends(get_db)):
    async with db as session:
        query = select(MoranguinhoModel).filter(MoranguinhoModel.id == moranguinho_id)
        result = await session.execute(query)
        moranguinho_up = result.scalar_one_or_none()
        
        
        if moranguinho_up:
            moranguinho_up.nome = moranguinho.nome
            moranguinho_up.ano = moranguinho.ano
            
            await session.commit()
            return moranguinho_up
        else:
            raise HTTPException(detail="moranguinho Não Encontrada",status_code=status.HTTP_404_NOT_FOUND)
        
        
@router.delete("/{moranguinho_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_moranguinho(moranguinho_id: int, db: Session= Depends(get_db)):
    async with db as session:    
        query= select(MoranguinhoModel).filter(MoranguinhoModel.id == moranguinho_id)
        result = await session.execute(query)
        moranguinho_del = result.scalar_one_or_none()
        
        if moranguinho_del:
            await session.delete(moranguinho_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="moranguinho Não Encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
        
         
        
        