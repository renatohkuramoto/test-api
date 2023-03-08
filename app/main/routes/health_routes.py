from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter(
    responses={},
    tags=['Health']
)


@router.get('/health-check', status_code=HTTPStatus.OK)
def health():
    return 'Ok'
