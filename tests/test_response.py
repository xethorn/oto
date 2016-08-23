from unittest.mock import patch

import pytest

from oto import response
from oto import error


def test_response_creation():
    """Test the default response creation.
    """

    resp = response.Response()
    assert not resp.message
    assert not resp.errors
    assert resp
    assert resp.status == 200


def test_response_creation_with_message():
    """Test the creation of a response with a message.
    """

    message = 'something'
    resp = response.Response(message=message)
    assert resp
    assert resp.message == message
    assert resp.status == 200


def test_response_creation_with_errors():
    """Test the response creation with errors.
    """

    error = 'something'
    resp = response.Response(errors=error)
    assert not resp.message
    assert not resp
    assert resp.errors == error
    assert resp.status == 400  # default


def test_response_creation_with_status():
    """Test the response creation with a defined status.
    Within the 200's, the response is considered valid. Above it's invalid.
    """

    for status in range(200, 300):
        resp = response.Response(status=status)
        assert resp
        assert resp.status == status

    for status in range(300, 500):
        resp = response.Response(status=status)
        assert not resp
        assert resp.status == status


@pytest.mark.parametrize('call, status, code', [
    (response.create_fatal_response, 500, error.ERROR_CODE_INTERNAL_ERROR),
    (response.create_not_found_response, 404, error.ERROR_CODE_NOT_FOUND)])
def test_create_error_response(call, status, code):
    """Test the creation of a fatal response.
    """

    error_message = 'something'

    resp = call()
    assert not resp
    assert resp.status == status

    resp = call(error_message)
    assert resp.errors.get('code') == code
    assert resp.errors.get('message') == error_message


def test_custom_error_response():
    """Test creating a custom error response.
    """

    error_message = 'something'
    resp = response.create_error_response('code', error_message)
    assert resp.errors.get('code') == 'code'
    assert resp.errors.get('message') == error_message
