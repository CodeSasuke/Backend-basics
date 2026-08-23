"""Exercise implementation: extend the HTTP service."""

from http.server import BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    """TODO: implement health, account creation, and balance endpoints."""

    def do_GET(self) -> None:
        raise NotImplementedError

    def do_POST(self) -> None:
        raise NotImplementedError
