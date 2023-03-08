from pydantic import BaseModel


class GenericErrorResponse(BaseModel):
    error: str
