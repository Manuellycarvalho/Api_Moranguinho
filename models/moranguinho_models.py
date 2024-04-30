from core.configs import settings
from sqlalchemy import Column, Integer,String
from create_db import Base

# class MoranguinhoModel(settings.DBBaseModel):
class MoranguinhoModel(Base):
    __tablename__ = 'moranguinho'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome: str = Column(String(100))
    residencia: str = Column(String(100))
    genero: str = Column(String(100))
    ocupacao: str  = Column(String(100))
    aparencia: str = Column(String(100))
    personalidade: str = Column(String(100))
    animais_de_estimacao: str = Column(String(100))