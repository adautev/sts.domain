from typing import List

from domain.infrastructure.location.stop_location import StopLocation


class Route(object):
    def __init__(self, name: str, stop_locations:List[StopLocation]):
        self.name = name
        self.stop_locations = stop_locations

