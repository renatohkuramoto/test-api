from http import HTTPStatus

from sqlalchemy.orm import Session

from app.domain.usecases import GetUserContract, GetUserParams
from library.helpers.http import HttpError, HttpResponse, HttpStatus
from library.helpers.log import logger
from library.repositories import UserRepositoryContract


class GetUser(GetUserContract):
    def __init__(
        self,
        user_repository: UserRepositoryContract,
        session_db: Session
    ) -> None:
        self._user_repository = user_repository
        self._session_db = next(session_db)

    def execute(self, params: GetUserParams) -> HttpResponse:

        try:
            user = self._user_repository.find_by_email(db=self._session_db, email=params.email)
            if user:
                response = self._user_repository.to_dict(user)
                return HttpStatus.ok_200(body=response)
            return HttpStatus.not_found_404(custom_msg='User not found!')
        except Exception as error:
            logger.info(error)
            raise HttpError(HTTPStatus.BAD_REQUEST, error)
