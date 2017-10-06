import json
from mock import patch

from oto import response
from oto.adaptors import flask_adapter


def test_flaskify_dict_response():
    """Test flaskifying a response.
    """

    resp = flask_adapter.flaskify(response.Response(message=dict(key='value')))
    assert resp.data == b'{"key": "value"}'
    assert resp.mimetype == 'application/json'
    assert resp.status_code == 200


def test_flaskify_list_response():
    """Test flaskifying a response.
    """

    resp = flask_adapter.flaskify(response.Response(message=['value1', 'value2']))
    assert resp.data == b'["value1", "value2"]'
    assert resp.mimetype == 'application/json'
    assert resp.status_code == 200


def test_flaskify_string_response():
    """Test flaskifying a response.
    """

    resp = flask_adapter.flaskify(response.Response(message='value1'))
    assert resp.data == b'value1'
    assert resp.mimetype == 'text/plain'
    assert resp.status_code == 200


def test_flaskify_error_response():
    """Flaskify an error response.
    """

    resp = flask_adapter.flaskify(response.create_fatal_response('Fatal Error'))
    assert resp.status_code == 500

    data = json.loads(resp.data.decode('utf8'))
    assert data == {'message': 'Fatal Error', 'code': 'internal_error'}
