from pydantic import BaseModel

class MoranguinhoSchema(BaseModel):
    nome: str
    residencia: str
    genero: str
    ocupacao: str
    aparencia: str
    personalidade: str
    animais_de_estimacao: str
    
class MoranguinhoRequest(MoranguinhoSchema):    
    ...

class MoranguinhoResponse(MoranguinhoSchema):
    id: int


    class Config:
        orm_mode = True
