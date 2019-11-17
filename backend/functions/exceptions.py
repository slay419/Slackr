#pylint: disable=missing-docstring
from json import dumps
from werkzeug.exceptions import HTTPException

# Class for ValueError handling
class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

# Class for AccessError handling
class AccessError(HTTPException):
    code = 400
    message = 'No message specified'


def default_handler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response
