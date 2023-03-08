from http import HTTPStatus
from typing import Any, Dict, Optional


class HttpRequest:
    def __init__(self, header: Optional[Dict] = None, body: Optional[Dict] = None, query: Optional[Dict] = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )


class HttpResponse:

    def __init__(self, status_code: int, body: Any = None, headers: Dict[str, str | int] | None = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body}), headers={self.headers}"


class HttpError(Exception):
    def __init__(
        self,
        status_code: int,
        message: str = HTTPStatus.INTERNAL_SERVER_ERROR.phrase
    ):
        self.status_code = status_code
        self.message = message

    def __repr__(self):
        return f'HttpError (status_code={self.status_code}, message={self.message})'


class HttpStatus:
    @staticmethod
    def ok_200(body: Optional[Any] = None, headers: Dict[str, str | int] | None = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, body, headers=headers)

    @staticmethod
    def created_201(body: Optional[Any] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.CREATED, body)

    @staticmethod
    def bad_request_400(custom_msg: Optional[str] = None, body: Any = None) -> HttpResponse:
        if body:
            return HttpResponse(HTTPStatus.BAD_REQUEST, body)
        return HttpResponse(HTTPStatus.BAD_REQUEST, {"error": custom_msg or "Bad Request"})

    @staticmethod
    def unauthorized_401(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.UNAUTHORIZED, {"error": custom_msg or "Unauthorized"})

    @staticmethod
    def forbidden_403(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.FORBIDDEN, {"error": custom_msg or "Forbidden"})

    @staticmethod
    def not_found_404(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.NOT_FOUND, {"error": custom_msg or "Not Found"})
