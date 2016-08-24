"""
Statuses
========

Statuses describe the state of the data. It gives an additional information
that can be later on used. For simplicity, the statuses are borrowed from the
HTTP specification, as it already provides an extensive list.

Not all statuses might be useful, but we have added a few to make it easier.
"""

CONTINUE = 100
PROCESSING = 102

OK = 200
CREATED = 201
ACCEPTED = 202
NON_AUTHORITATIVE = 203
NO_CONTENT = 204
RESET_CONTENT = 205
PARTIAL_CONTENT = 206
MULTIPLE_STATUS = 207
ALREADY_REPORTED = 208

BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
NOT_ACCEPTABLE = 406
PROXY_AUTHENTICATION_REQUIRED = 407
REQUEST_TIMEOUT = 408
CONFLICT = 409
GONE = 410

INTERNAL_ERROR = 500
NOT_IMPLEMENTED = 501
BAD_GATEWAY = 502
SERVICE_UNAVAILABLE = 503
GATEWAY_TIMEOUT = 504
