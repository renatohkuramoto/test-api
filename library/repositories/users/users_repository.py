from typing import Dict

from sqlalchemy.orm import Session

from library.models import Users

from .user_repository_contract import UserRepositoryContract


class UserRepository(UserRepositoryContract):
    @staticmethod
    def find_all(db: Session) -> list[Users]:
        return db.query(Users).all()

    @staticmethod
    def save(db: Session, user: Users) -> Users:
        if user.id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()
        return user

    @staticmethod
    def find_by_id(db: Session, id: int) -> Users:
        return db.query(Users).filter(Users.id == id).first()
    
    @staticmethod
    def find_by_email(db: Session, email: str) -> Users:
        return db.query(Users).filter(Users.email == email).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Users).filter(Users.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Users).filter(Users.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()
    
    @staticmethod
    def to_dict(user: Users) -> Dict:
        return {
            'id': user.id,
            'first_name': user.first_name,
            'second_name': user.second_name,
            'email': user.email,
            'phone': user.phone
        }
