from sqlalchemy.orm import Session

from models.moranguinho_models import MoranguinhoModel


class MoranguinhoRepository:
    @staticmethod
    def find_all(db: Session) -> list[MoranguinhoModel]:
        return db.query(MoranguinhoModel).all()
    

    @staticmethod
    def save(db: Session, moranguinho: MoranguinhoModel) -> MoranguinhoModel:
        if moranguinho.id:
            db.merge(moranguinho)

        else:
            db.add(moranguinho)
        db.commit()
        return moranguinho
        

    @staticmethod
    def find_by_id(db: Session, id:int) -> MoranguinhoModel:
        return db.query(MoranguinhoModel).filter(MoranguinhoModel.id == id).first()
    

    @staticmethod
    def exists_by_id (db: Session, id: int) -> bool:
        return db.query(MoranguinhoModel).filter(MoranguinhoModel.id == id).first() is not None
    
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        moranguinho = db.query(MoranguinhoModel).filter(MoranguinhoModel.id== id).filter()
        if moranguinho is not None:
            db.delete(moranguinho)
            db.commit()