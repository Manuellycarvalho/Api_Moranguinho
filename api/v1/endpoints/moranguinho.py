from typing import List 
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import session
from sqlalchemy.future import select

from models.moranguinho_models import MoranguinhoModel
from schemas.moranguinho_schema import MoranguinhoSchema
from core.deps import get_session
from create_db import get_db

from create_db import SessionLocal, engine

router = APIRouter()



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MoranguinhoSchema) 
async def post_moranguinho(moranguinho: MoranguinhoSchema, db: Session = Depends(get_db)):
    nova_moranguinho = MoranguinhoModel(**moranguinho.dict())
    db.add(nova_moranguinho)
    await db.commit()
    
    return nova_moranguinho

@router.get("/", response_model=List[MoranguinhoSchema])
async def get_moranguinho(db: Session = Depends(get_db)):
    query = select(MoranguinhoModel)
    result = await db.execute(query)
    moranguinhos = result.scalars().all()
    
    return moranguinhos

@router.get("/{moranguinho_id}", response_model=MoranguinhoSchema, status_code=status.HTTP_200_OK)
async def get_moranguinho(moranguinho_id: int, db: Session = Depends(get_db)):
    query = select(MoranguinhoModel).filter(MoranguinhoModel.id == moranguinho_id)
    result = await db.execute(query)
    moranguinho = result.scalar_one_or_none()
    
    if moranguinho:
        return moranguinho
    else:
        raise HTTPException(detail="Moranguinho não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{moranguinho_id}", response_model=MoranguinhoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_moranguinho(moranguinho_id: int, moranguinho: MoranguinhoSchema, db: Session = Depends(get_db)):
    query = select(MoranguinhoModel).filter(MoranguinhoModel.id == moranguinho_id)
    result = await db.execute(query)
    moranguinho_up = result.scalar_one_or_none()
    
    if moranguinho_up:
        for field, value in moranguinho.dict().items():
            setattr(moranguinho_up, field, value)
        await db.commit()
        return moranguinho_up
    else:
        raise HTTPException(detail="Moranguinho não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{moranguinho_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_moranguinho(moranguinho_id: int, db: Session = Depends(get_db)):
    query = select(MoranguinhoModel).filter(MoranguinhoModel.id == moranguinho_id)
    result = await db.execute(query)
    moranguinho_del = result.scalar_one_or_none()
    
    if moranguinho_del:
        await db.delete(moranguinho_del)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail="Moranguinho não encontrada", status_code=status.HTTP_404_NOT_FOUND)

        
         
        
        