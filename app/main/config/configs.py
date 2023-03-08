from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from pydantic import schema

import app.main.routes as routes
from library.helpers.log import logger


def hidden_schema_config():
    def field_schema(field, **kwargs):
        if field.field_info.extra.get('hidden_from_schema', False):
            raise schema.SkipField(f'{field.name} field is being hidden')
        else:
            return original_field_schema(field, **kwargs)
    original_field_schema = schema.field_schema
    schema.field_schema = field_schema


def custom_openapi(app: FastAPI):
    def custom_docs():
        if not app.openapi_schema:
            app.openapi_schema = get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                terms_of_service=app.terms_of_service,
                contact=app.contact,
                license_info=app.license_info,
                routes=app.routes,
                tags=app.openapi_tags,
                servers=app.servers,
            )
            for _, method_item in app.openapi_schema.get('paths', {}).items():
                for _, param in method_item.items():
                    responses = param.get('responses')
                    if '422' in responses:
                        del responses['422']
        return app.openapi_schema

    app.openapi = custom_docs


def exception_config(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.warning(f'Parâmetros inválidos: {exc}')
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({
                'errors': [{
                    'field': error['loc'],
                    'error': error['msg']
                } for error in exc.errors()],
            }),
        )


def apply_routes_config(app: FastAPI):
    route_definitions = [
        getattr(routes, variable) for variable in dir(routes) if not variable.startswith('__')
    ]
    for router in route_definitions:
        try:
            app.include_router(router.router)
        except Exception:
            pass
