import json

from http import HTTPStatus

from encoder import Encoder


def response(code: int, message: str = '', data: [dict, list] = None) -> tuple:
    body = {
        'meta': {
            'code': code
        }
    }

    if message:
        body['meta']['message'] = message

    if data is not None:
        body['response'] = data

    body = json.dumps(body, sort_keys=True, cls=Encoder)
    body = json.loads(body)

    return body, code


def bad_request(message: str = 'Bad Request', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.BAD_REQUEST, message=message, data=data)


def conflict(message: str = 'Conflict', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.CONFLICT, message=message, data=data)


def forbidden(message: str = 'Forbidden', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.FORBIDDEN, message=message, data=data)


def not_found(message: str = 'Not Found', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.NOT_FOUND, message=message, data=data)


def ok(message: str = 'OK', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.OK, message=message, data=data)


def service_unavailable(message: str = 'Service Unavailable', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.SERVICE_UNAVAILABLE, message=message, data=data)


def unathorized(message: str = 'Unathorized', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.UNAUTHORIZED, message=message, data=data)
