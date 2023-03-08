from sqlalchemy import Column, Integer, String

from library.infra.database import Base


class Users(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    first_name: str = Column(String(100), nullable=False)
    second_name: str = Column(String(100), nullable=True)
    email: str = Column(String, nullable=False, unique=True)
    phone: int = Column(Integer, nullable=False)
