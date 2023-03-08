from app.services.usecases.user import GetUser
from library.infra.database import get_db
from library.repositories import UserRepository


def get_user_factory():
    return GetUser(
        user_repository=UserRepository(),
        session_db=get_db()
    )
