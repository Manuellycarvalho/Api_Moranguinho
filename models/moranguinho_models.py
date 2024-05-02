from core.configs import settings
from sqlalchemy import Column, Integer,String
from create_db import Base

# class MoranguinhoModel(settings.DBBaseModel):
class MoranguinhoModel(Base):
    __tablename__ = 'moranguinho'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome: str = Column(String(100),nullable=False)
    residencia: str = Column(String(100),nullable=False)
    genero: str = Column(String(100),nullable=False)
    ocupacao: str  = Column(String(100),nullable=False)
    aparencia: str = Column(String(100),nullable=False)
    personalidade: str = Column(String(100),nullable=False)
    animais_de_estimacao: str = Column(String(100),nullable=False)