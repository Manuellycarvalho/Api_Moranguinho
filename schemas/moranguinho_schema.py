from typing import Optional
from pydantic import BaseModel as SCBaseModel

class MoranguinhoSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    residencia: str
    genero: str
    ocupacao: str
    aparencia: str
    personalidade: str
    animais_de_estimacao: str
    
    class Config:
        orm_mode = True 