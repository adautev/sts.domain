from typing import List

from domain.exceptions.exception_codes import ExceptionCodes
from domain.infrastructure.routes.route import Route


class TravelPath(object):
    def __init__(self, routes: List[Route], circular: bool):
        self.routes = routes
        if len(self.routes) < 1:
            raise ValueError(320001)
        if len(self.routes) == 1 and not circular:
            raise ValueError(320002)
