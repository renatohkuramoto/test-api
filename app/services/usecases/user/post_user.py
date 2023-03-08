from http import HTTPStatus

from sqlalchemy.orm import Session

from app.domain.usecases import PostUserContract, PostUserParams
from library.helpers.http import HttpError, HttpResponse, HttpStatus
from library.helpers.log import logger
from library.models import Users
from library.repositories import UserRepositoryContract


class PostUser(PostUserContract):
    def __init__(
        self,
        user_repository: UserRepositoryContract,
        session_db: Session
    ) -> None:
        self._user_repository = user_repository
        self._session_db = next(session_db)

    def execute(self, params: PostUserParams) -> HttpResponse:
        try:
            user = self._user_repository.find_by_email(db=self._session_db, email=params.email)
            if user:
                return HttpStatus.bad_request_400(custom_msg='User already registered!')
            user = self._user_repository.save(db=self._session_db, user=Users(**params.dict()))
            print(user)
            response = self._user_repository.to_dict(user)
            return HttpStatus.created_201(body=response)
        except Exception as error:
            logger.info(error)
            raise HttpError(HTTPStatus.BAD_REQUEST, error)
