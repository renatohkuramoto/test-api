from http import HTTPStatus

from fastapi import APIRouter, Request, Response

from app.domain.usecases import GetUserParams, PostResponse, PostUserParams
from app.main.adapters import fast_api_adapter
from app.main.factories import get_user_factory, post_user_factory
from library.helpers.http import GenericErrorResponse

router = APIRouter(
    responses={},
    tags=['User']
)

@router.post(
    '/user',
    status_code=HTTPStatus.CREATED,
    responses={
        HTTPStatus.CREATED.value: {
            'model': PostResponse
        },
        HTTPStatus.BAD_REQUEST.value: {
            'model': GenericErrorResponse
        }
    },
)
def get_user(request: Request, response: Response, body: PostUserParams):
    return fast_api_adapter(body, response, post_user_factory())


@router.get(
    '/user/{email}',
    status_code=HTTPStatus.OK,
    responses={
        HTTPStatus.OK.value: {
            'model': PostResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'model': GenericErrorResponse
        }
    }
)
def get_user(request: Request, response: Response, email: str):
    params = GetUserParams(email=email)
    return fast_api_adapter(params, response, get_user_factory())
