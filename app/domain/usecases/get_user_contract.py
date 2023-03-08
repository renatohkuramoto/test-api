from abc import abstractmethod

from pydantic import Field

from app.domain.usecases.usecase import (NOT_IMPLEMENTED_ERROR, InputData,
                                         Usecase)
from library.helpers.http import HttpResponse


class GetUserParams(InputData):
    email: str = Field(hidden_from_schema=True, default=None)


class GetUserContract(Usecase):
    @abstractmethod
    def execute(self, params: GetUserParams) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
