import datetime

from domain.infrastructure.location.stop_location import StopLocation
from domain.infrastructure.location.stop_location_type import StopLocationType


class StopLocationOnTravelPath(StopLocation):
    def __init__(self, longtitude, latitude, arrival_time:datetime, departure_time:datetime, name="", location_type = StopLocationType.STOP):
        """
        Initializes a stop location on travel path - a geographical coordinate represented by an arrival and departure time.
        :param longtitude:
        :type longtitude: int
        :param latitude:
        :type latitude: int
        :param arrival_time:
        :type arrival_time:
        :param departure_time:
        :type departure_time:
        :param name:
        :type name: str
        :param location_type:
        :type location_type:
        """
        if departure_time < arrival_time:
            raise ValueError(150000)
        self.type = location_type
        self.arrival_time = arrival_time
        self.departure_time = departure_time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

