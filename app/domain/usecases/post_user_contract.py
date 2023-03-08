from abc import abstractmethod

from pydantic import BaseModel, Field

from app.domain.usecases.usecase import (NOT_IMPLEMENTED_ERROR, InputData,
                                         Usecase)
from library.helpers.http import HttpResponse


class PostUserParams(InputData):
    first_name: str = Field(description='Primeiro Nome.')
    second_name: str = Field(description='Sobrenome.')
    email: str = Field(description='E-mail.')
    phone: int = Field(description='Telefone.')


class PostResponse(BaseModel):
    id: int
    first_name: str
    second_name: str
    email: str
    phone: int


class PostUserContract(Usecase):
    @abstractmethod
    def execute(self, params: PostUserParams) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
