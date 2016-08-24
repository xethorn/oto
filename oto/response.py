"""
Response
========

Response is an object that helps passing data between different layers of your
application while preserving a specific state. Response contains 3 main fields:
message (data), errors (any errors that might have been found), and a status.

Usage:

    resp = Response(errors='Something', status=200)
    bool(resp) # False
    resp.status # 400
    resp = Response()
    bool(resp) # True
    resp.status # 200
"""

import json

from oto import error
from oto import status


class Response:

    def __init__(self, message=None, errors=None, status=None):
        """Create a response object.

        Args:
            message: the message object (it could be any type of object.)
            errors: the errors to attach (it could be any type of object.)
            status (int): the status of the response. Errors should use the
                status that is the most appropriate. System failures should
                set a 500.
        """

        self.status = status or 200
        self.message = message
        self.errors = errors

        if self.errors and self.status == 200:
            self.status = 400

    def __bool__(self):
        """If the request has been successful.

        Returns:
            boolean: if the response is considered successful.
        """

        return 200 <= self.status < 300 and not self.errors


def create_fatal_response(message=None):
    """Create a fatal response.

    Args:
        message: the error to add (it could be any type of object, from string
            to dict.)

    Returns:
        Response: the fatal error response object.
    """

    return create_error_response(
        error.ERROR_CODE_INTERNAL_ERROR, message,
        status=status.INTERNAL_ERROR)


def create_error_response(code, message, status=status.BAD_REQUEST):
    """Create a fail response.

    Args:
        code (str): the code of the error. The title should be lowercase and
            underscore separated.
        message (dict, list, str): the message of the error.
            This can be a list, dictionary or simple string.
        status (int): the status code. Defaults to 400.

    Returns:
        Response: the response with the error. The format of the error is the
            following: code and message. The code could be `user_error` or
            `internal_error`. The message contains either a string, or a list
            or a dictionary. If not specify, the status will be a 400.
    """

    errors = dict(code=code, message=message)
    return Response(errors=errors, status=status)


def create_not_found_response(message=None):
    """Create a not found response.

    Args:
        message: The errors to add (it could be any type of object, from
            strings to dict.)

    Returns:
        Response: the “not found” response object.
    """

    return create_error_response(
        error.ERROR_CODE_NOT_FOUND, message, status=status.NOT_FOUND)
