from domain.infrastructure.location.stop_location import StopLocation
from domain.service.timetable_planning.trip import Trip


class Connection(object):
    """
    Represents a relationship between a trip and
    """
    def __init__(self, connecting_trip_a: Trip, connecting_trip_b: Trip, connection_point: StopLocation ):
        self.connecting_trip_a = connecting_trip_a
        self.connecting_trip_b = connecting_trip_b
        self.connection_point = connection_point
        if connecting_trip_a.travel_path is None:
            raise ValueError(520001)
        if connecting_trip_a.travel_path.routes is None:
            raise ValueError(520002)
        if connecting_trip_b.travel_path is None:
            raise ValueError(520003)
        if connecting_trip_b.travel_path.routes is None:
            raise ValueError(520004)
        # TODO: Start here foo(l) :D