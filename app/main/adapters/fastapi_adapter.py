
from http import HTTPStatus
from traceback import format_exc
from typing import Any

from fastapi import Response

from app.domain.usecases import Usecase
from library.helpers.http import HttpError
from library.helpers.log import logger


def fast_api_adapter(params: object, response: Response, usecase: Usecase) -> Any:
    try:
        logger.info(f'Params: {params}')
        usecase_response = usecase.execute(params)
        response.status_code = usecase_response.status_code
        logger.info(f'Response: {usecase_response}')
        return usecase_response.body if usecase_response.body else response
    except HttpError as error:
        logger.warning(
            f'Erro previstro do caso de uso: {error.status_code} - {error.message}')
        logger.warning(f'{format_exc()}')
        response.status_code = error.status_code
        return {'message': error.message} if error.message else response

    except Exception:
        logger.error(
            f'Erro desconhecido na execução do caso de uso: {format_exc()}')
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': 'Internal server error'}
