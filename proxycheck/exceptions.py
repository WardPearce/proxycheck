class ProxyCheckException(Exception):
    """Base exception.
    """

    pass


class QueryFailed(ProxyCheckException):
    """Raised when status is error.
    """

    pass


class QueryDenied(ProxyCheckException):
    """Raised when status is denied.
    """

    pass
