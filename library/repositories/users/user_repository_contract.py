from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import Session

from library.models import Users

NOT_IMPLEMENTED_ERROR = 'This contract method must be implemented'

class UserRepositoryContract(ABC):
    @staticmethod
    @abstractmethod
    def find_all(db: Session) -> list[Users]:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @staticmethod
    @abstractmethod
    def save(db: Session, user: Users) -> Users:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @staticmethod
    @abstractmethod
    def find_by_id(db: Session, id: int) -> Users:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
    
    @staticmethod
    @abstractmethod
    def find_by_email(db: Session, email: str) -> Users:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @staticmethod
    @abstractmethod
    def exists_by_id(db: Session, id: int) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @staticmethod
    @abstractmethod
    def delete_by_id(db: Session, id: int) -> None:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    @staticmethod
    @abstractmethod
    def to_dict(user: Users) -> Dict:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
