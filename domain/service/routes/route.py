from typing import List

from domain.infrastructure.location.stop_location_on_travel_path import StopLocationOnTravelPath


class Route(object):
    def __init__(self, name: str, stop_locations:List[StopLocationOnTravelPath]):
        self.name = name
        self.stop_locations = stop_locations

