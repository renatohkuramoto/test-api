from app.services.usecases.user import PostUser
from library.infra.database import get_db
from library.repositories import UserRepository


def post_user_factory():
    return PostUser(
        user_repository=UserRepository(),
        session_db=get_db()
    )
